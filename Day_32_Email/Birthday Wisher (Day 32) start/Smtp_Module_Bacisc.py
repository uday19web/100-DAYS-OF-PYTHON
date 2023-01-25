import smtplib

my_email = "udayudemycourse@gmail.com"
password = "lzifbzgaysuspjom"
to_email = "uday_udemy_course@yahoo.com"

'''
# intiate the connetion
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs=to_email,
                    msg="Subject:Hello\n\nI am sending mail from gmail using python code.")
connection.close()
'''
# with keyword no need to close the connection it will automatically will close
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg="Subject:Hello\n\nI am sending mail from gmail using python code.")