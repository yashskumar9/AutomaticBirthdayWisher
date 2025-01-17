import smtplib
import pandas
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_NAME = "[NAME]"
BIRTHDAY_QUOTE = "[QUOTE]"
new_mail = []

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')

today_date = dt.datetime.now()
month = today_date.month
date = today_date.day

data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")

with open("birthday_wishes.txt", encoding='utf-8') as birthday_quotes_file:
    quotes_data = birthday_quotes_file.readlines()
    new_quote = [quote.strip("\n") for quote in quotes_data]
    random_quote = random.choice(quotes_data)

for person in birthday_data:
    if person['month'] == month and person['day'] == date:
        with open("letter.txt") as letter_file:
            letter_content = letter_file.read()
            changed_quote = letter_content.replace(BIRTHDAY_QUOTE, random_quote)
            new_mail = changed_quote.replace(SENDER_NAME, person['name'])

        receiver_email = person['email']

        message = f"Subject: Happy Birthday!!! 🥳 \n\n{new_mail}".encode('utf-8')

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_email,
                msg=message)
