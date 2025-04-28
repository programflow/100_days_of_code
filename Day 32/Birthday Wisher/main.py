import smtplib
import datetime as dt
import pandas as pd
from random import choice, randint


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
my_email = "johndoedothough@gmail.com"
password = "phbeoypovugbianb"
connection = smtplib.SMTP("smtp.gmail.com")
now=dt.datetime.now()

def find_birthday():
    birthdays = pd.read_csv('birthdays.csv')
    birthday_month_check = birthdays.month == now.month
    birthday_day_check = birthdays.day == now.day

    if now.month in birthdays.month.tolist() and now.day in birthdays.day.tolist():
        birthday_name = birthdays[(birthday_day_check) & (birthday_month_check)].iloc[0]["name"]
        birthday_email = birthdays[(birthday_day_check) & (birthday_month_check)].iloc[0]["email"]
        return birthday_email, birthday_name
    else:
        return None, None



bday_email, birthday_person = find_birthday()
if birthday_person is not None:
    print("happy birthday {}".format(birthday_person))
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    random_letter = randint(1,3)
    with open(f"letter_templates/letter_{random_letter}.txt","r") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person)



    connection.starttls()
    connection.login(user=my_email, password=password)
    message = f"Subject:Hello\n\n{letter}."
    connection.sendmail(
        from_addr=my_email,
        to_addrs=bday_email,
        msg=message
    )
    connection.close()



# 4. Send the letter generated in step 3 to that person's email address.




