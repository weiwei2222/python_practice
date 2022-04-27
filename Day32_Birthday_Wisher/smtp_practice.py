import smtplib

my_email = "linweiwei2222@gmail.com"
password = "lin855146"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="linweiwei2222@163.com",
        msg="Subject:Hello\n\nThis is test"
    )

# import datetime as dt
#
# my_time = dt.datetime.now()
# year = my_time.year
# month = my_time.month
# week = my_time.weekday()
# day = my_time.day
# print(year)
# print(month)
# print(week)
# print(day)
#
# data_of_birth = dt.datetime(year=1985, month=10, day=3, hour=14)
# print(data_of_birth)