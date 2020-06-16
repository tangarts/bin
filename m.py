#!/usr/bin/env python3

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PORT = 587  # For starttls
SMTP_SERVER = "smtp.office365.com"
SENDER_EMAIL = ""
RECEIVER_EMAIL =  ""
PASSWORD = input("Type your password and press enter:")


subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"


# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL
message["Subject"] = subject
#message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

# part = MIMEBase()
# part.add_header("Content-Disposition")
# messsage.attach(part)

text = message.as_string()


context = ssl.create_default_context()
with smtplib.SMTP(SMTP_SERVER, PORT) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(SENDER_EMAIL, PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)

print("success!")
