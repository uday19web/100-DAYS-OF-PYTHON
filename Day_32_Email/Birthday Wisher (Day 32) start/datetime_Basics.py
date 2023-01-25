import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2023:
    print("Hi")
print(type(year))
print(now)
month = now.month
day_of_week = now.weekday()
print(month, day_of_week)# computer start with 0 it means monday

# creating our own object from scratch
date_of_birth = dt.datetime(year=1991, month=6, day=19, hour=6)
print(date_of_birth)