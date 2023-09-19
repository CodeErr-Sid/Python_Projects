from datetime import datetime
import pandas
import random
import smtplib

today = (datetime.now().month, datetime.now().day)

MY_MAIL = "siddiquetestemail@gmail.com"
MY_PASS = "kdox juvy mjln unxt"


data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
  birthday_person = birthday_dict[today]
  file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[Name]", birthday_person["name"])

  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_MAIL, MY_PASS)
    connection.sendmail(from_addr= MY_MAIL, 
                        to_addrs= birthday_person["email"] ,
                        msg= f"Subject:HAPPY BIRTHDAY!\n\n{contents}")
