from datetime import datetime
import random
import smtplib
import pandas

SENDER_NAME = 'your_name'
SMTP_SERVER_INFO = 'smtp.gmail.com'
SENDER_EMAIL = 'your@gmailaddress.org'
SENDER_PASSWORD = 'your_gmail_password'

today_tuple = (datetime.now().month, datetime.now().day)

# read birthdays.csv
data = pandas.read_csv("birthdays.csv")
# create a dictionary from the data frame: { (month, day): data_row }
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
# check if today tuple (=today's date) matches any keys (=birthdays) in the dictionary
if today_tuple in birthdays_dict:
    # pick a random letter template
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # update letter contents with correct names
        recipient = birthdays_dict[today_tuple]
        recipient_name = recipient['name']
        recipient_email = recipient['email']
        contents = contents.replace('[NAME]', recipient_name)
        contents = contents.replace('[SENDER]', SENDER_NAME)

    # send email to the recipient
    with smtplib.SMTP(SMTP_SERVER_INFO) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=recipient_email, msg=f"Happy Birthday\n\n{contents}")
