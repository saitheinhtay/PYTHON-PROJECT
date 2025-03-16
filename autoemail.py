import os
import random
import smtplib

from bitmapmessage import message


def automatic_email():
    user = input('Enter your name : ')
    email = input('Enter Your Email : ')
    message = (f'Dear {user}, Welcome to The Clever Programmer ')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('nampnaung@gmail.com', 'Thy@285138')
    s.sendmail('&&&&&&&&', email, message)
    print('Email Sent! ')

automatic_email()