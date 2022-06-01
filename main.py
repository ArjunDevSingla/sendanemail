import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email from Python!"
sender_email = "jaisingla1107@gmail.com"
reciever_email = "arjundevsingla1612@gmail.com"
password = input("Type Password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string())

print("Success")