import smtplib
from email.mime.text import MIMEText
# from datetime import datetime
from GMAIL_PWD import GMAIL_PWD, MAIN_EMAIL, FROM_WHO


class GmailPerformance:
    """

    """
    def __init__(self, mailbox, psw, from_who):
        """

        """
        self.__mailbox = mailbox
        self.__password = psw
        self.__from_who = from_who

    def send_plaintext(self, mailbox_str, mail_subject_str, msg_str):
        """

        """
        msg = MIMEText(msg_str, 'plain')

        msg['Subject'] = mail_subject_str
        msg['From'] = self.__mailbox
        msg['To'] = mailbox_str

        server = smtplib.SMTP('smtp.gmail.com', port=587)

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.__mailbox, self.__password)
        msg["Received:"] = "from Windows 10 Pro ([200.200.200.200])"
        server.send_message(msg)
        server.close()


if __name__ == '__main__':
    mail = GmailPerformance(MAIN_EMAIL, GMAIL_PWD, FROM_WHO)
    mail.send_plaintext("pandrey76@yandex.ru", "Subject", "Hello, world")

