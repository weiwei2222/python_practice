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

