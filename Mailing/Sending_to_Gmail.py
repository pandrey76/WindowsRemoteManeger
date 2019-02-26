
import smtplib
from email.mime.text import MIMEText
# from datetime import datetime
from GMAIL_PWD import GMAIL_PWD, MAIN_EMAIL, FROM_WHO


def send_gmail(msg_str):
    msg = MIMEText(msg_str, 'plain')

    msg['Subject'] = FROM_WHO
    msg['From'] = MAIN_EMAIL
    msg['To'] = MAIN_EMAIL

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()  # Extended Hello
    server.starttls()  # Put the SMTP connection in TLS (Transport Layer Security) mode.
    server.ehlo()  # All SMTP comands that follow will be encrypted.
    # server.login('pintchukandrey76@gmail.com', GMAIL_PWD)
    server.login(MAIN_EMAIL, GMAIL_PWD)
    msg["Received:"] = "from Windows 10 Pro ([200.200.200.200])"
    server.send_message(msg)

    # server.mail("pinchukandreyurevich76@gmail.com", messages)
    server.close()


# def take_email()
# ===========================================
if __name__ == '__main__':
    #send_gmail("BAN")
    send_gmail("RECOVER")
