import smtplib
import datetime as dt
import pandas as pd
from random import choice
my_email = "johndoedothough@gmail.com"
password = "phbeoypovugbianb"
connection = smtplib.SMTP("smtp.gmail.com")
#TLS = Transport layer security => encrypts email
now=dt.datetime.now()
day_of_week = now.weekday()

def pick_quote():
    with open('quotes.txt') as file:
        data = file.readlines()

    return choice(data)



print(day_of_week)
if int(day_of_week) == 6:
    c

else:
    print("Not Sunday")



# now = dt.datetime.now()
# year = now.year
# month = now.month
#
# print(now)
# if year == 2020:
#     print("wear a face mask")
# print(type(now))
#
# date_of_birth = dt.datetime(year=1991, month=3, day=1, hour=4, minute=30, second=30)
# print(date_of_birth)