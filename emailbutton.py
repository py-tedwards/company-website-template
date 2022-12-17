import smtplib
import os


def email_me(message):
    user = 'tedwards0460@gmail.com'
    receivers = 'tedwards0460@gmail.com'
    password = os.getenv('PASSWORD')

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, receivers, message)
    server.close()