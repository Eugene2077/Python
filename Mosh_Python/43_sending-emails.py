

# mime: Multipurpose internet mail extensions (standard that define the format for email - not python, it is standard)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText   # 
import smtplib

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"]   = "aosk@mail.com"
message["subject"] = "email from my code"
message.attach(MIMEText("this is body part"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("eastonkelly@mail.com", "Asdfjk12!")
    smtp.send_message(message)
    print("Sent......")