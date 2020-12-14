
import smtplib
from email.mime.text import MIMEText

import os
import importlib.util

# from datetime import datetime
# from GMAIL_PWD import GMAIL_PWD, MAIN_EMAIL, FROM_WHO


def send_gmail(msg_str, to_mail="pandrey76@yandex.ru", subject="Windows service"):

    path_to_run_ps_script = os.path.dirname(os.path.realpath(__file__))
    path_to_run_ps_script = os.path.join(path_to_run_ps_script, 'GMAIL_PWD.py')
    spec = importlib.util.spec_from_file_location("GMAIL_PWD",
                                                  path_to_run_ps_script)
    gmail_pwd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gmail_pwd)

    msg = MIMEText(msg_str, 'plain')

    msg['Subject'] = subject
    msg['From'] = gmail_pwd.MAIN_EMAIL
    msg['To'] = to_mail

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()  # Extended Hello
    server.starttls()  # Put the SMTP connection in TLS (Transport Layer Security) mode.
    server.ehlo()  # All SMTP comands that follow will be encrypted.
    # server.login('pintchukandrey76@gmail.com', GMAIL_PWD)
    server.login(gmail_pwd.MAIN_EMAIL, gmail_pwd.GMAIL_PWD)
    msg["Received:"] = "from Windows 10 Pro ([200.200.200.200])"
    server.send_message(msg)

    # server.mail("pinchukandreyurevich76@gmail.com", messages)
    server.close()


# def take_email()
# ===========================================
if __name__ == '__main__':
    #send_gmail("BAN")
    send_gmail("UPDATE")

