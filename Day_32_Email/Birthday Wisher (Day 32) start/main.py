import smtplib, datetime as dt, random
FROM_EMAIL = "udayudemycourse@gmail.com"
PASSWORD = "lzifbzgaysuspjom"
TO_EMAIL = "uday_udemy_course@yahoo.com"

with open("quotes.txt", "r") as data:
    quotes = data.readlines()
    # print(quotes)
message = random.choice(quotes)

now = dt.datetime.now()
today = now.weekday()

def email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject:Motivational Quotes\n\n{message.strip()}")


if today == 2:
    email()
