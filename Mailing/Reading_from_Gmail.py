import imaplib
import email

import base64
import os
import importlib.util

import socket

#MAIN_EMAIL = "pinchukandreyurevich76@gmail.com"
#GMAIL_PWD = ""
#FROM_WHO = "Prapor"


class Mailing:
    def __init__(self):
        """

        """
        path_to_run_ps_script = os.path.dirname(os.path.realpath(__file__))

        path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'GMAIL_PWD.py')

        spec = importlib.util.spec_from_file_location("GMAIL_PWD",
                                                      path_to_run_ps_script)
        self.__gmail_pwd = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.__gmail_pwd)

        self.__Body = None



    mail_body = property(lambda self: self.__Body)
    """
    """

    def is_online(self):
        """

        :return:
        """
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("www.google.ru", 80), timeout=20)
            return True
        except OSError:
            pass
        return False

    def read_unseen_mail(self):
        """

        :return:
        """
        host = "imap.gmail.com"
        port = 993
        user = self.__gmail_pwd.MAIN_EMAIL
        password = self.__gmail_pwd .GMAIL_PWD
        sender = self.__gmail_pwd .MAIN_EMAIL

        connection = imaplib.IMAP4_SSL(host=host, port=port)
        connection.login(user=user, password=password)

        status, msgs = connection.select('INBOX')
        assert status == 'OK'

        typ, data = connection.search(None, '(UNSEEN)', 'FROM', '"%s"' % sender)
        try:
            for num in data[0].split():
                typ, message_data = connection.fetch(num, '(RFC822)')
                mail = email.message_from_bytes(message_data[0][1])
                for part in mail.walk():
                    self.__Body = part.get_payload(decode=True)
        finally:
            try:
                connection.close()
            except:
                pass
            connection.logout()


def read_gmail():
    host = "imap.gmail.com"
    port = 993
    user = MAIN_EMAIL
    password = GMAIL_PWD
    sender = MAIN_EMAIL

    connection = imaplib.IMAP4_SSL(host=host, port=port)
    connection.login(user=user, password=password)

    status, msgs = connection.select('INBOX')
    assert status == 'OK'

    typ, data = connection.search(None, '(UNSEEN)', 'FROM', '"%s"' % sender)
    body = ''
    try:
        print(data)
        for num in data[0].split():
            typ, message_data = connection.fetch(num, '(RFC822)')
            # print(data)
            print('Message %s\n%s\n' % (num, message_data[0][1]))
            mail = email.message_from_bytes(message_data[0][1])
            print("Mail" ,mail)
            for part in mail.walk():
                content_type = part.get_content_type()
                print(content_type)
                play_load = part.get_payload()
                print(play_load)
                print(part["Date"])
                print(part["Subject"])
                print(part["From"])
                print(part["To"])
                print(part["Content-Transfer-Encoding"])    #base64
                print(part["Received"])
                filename = part.get_filename()
                if filename:
                    print(filename)
                    # Нам плохого не надо, в письме может быть всякое барахло
                    with open(part.get_filename(), 'wb') as new_file:
                        new_file.write(part.get_payload(decode=True))

                # Первый способ декодтроавания тела сообщения
                if part["Content-Transfer-Encoding"] == "base64":
                    print("Variant 1:   ", base64.b64decode(play_load).decode("UTF-8"))

                # Второй способ декодирования ела сообщения (Более правильный)
                body = part.get_payload(decode=True)
                print("Variant 2:   ", part.get_payload(decode=True))

                # with open(str(num), 'wb') as new_file:
                #    new_file.write(part.get_payload(decode=True))

    finally:
        try:
            connection.close()
        except:
            pass
        connection.logout()
        return body


if __name__ == '__main__':

    mail = Mailing()
    flag = mail.is_online()
    print(flag)
    #mail.read_unseen_mail()
    #body = mail.mail_body
    #print(body)
