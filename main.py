import smtplib

my_mail = "example@gmail.com"
password = "1q2w3e4r"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="destinaion@gmail.com",
                        msg="Subject:Hello\n\nStart typing your message")



