import datetime as dt

my_time = dt.datetime.now()
year = my_time.year
month = my_time.month
week = my_time.weekday()
day = my_time.day
print(year)
print(month)
print(week)
print(day)

data_of_birth = dt.datetime(year=1985, month=10, day=3, hour=14)
print(data_of_birth)