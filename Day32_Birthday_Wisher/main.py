import datetime
import random
import smtplib
import datetime as dt
import pandas

my_email = "linweiwei2222@gmail.com"
password = "lin855146"
today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(4, 26), Lily,linweiwei2222@163.com,1985,4,26}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_contents}"
        )
