import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config

SERVER_EMAIL_USERNAME = config("SERVER_EMAIL_USERNAME")
SERVER_EMAIL_PASSWORD = config("SERVER_EMAIL_PASSWORD")


class Email:
    @staticmethod
    def send_email(subject: str, msg: str, receiver: str) -> None:
        host = "smtp.gmail.com"
        port = 465
    
        username = SERVER_EMAIL_USERNAME
        password = SERVER_EMAIL_PASSWORD
    
        context = ssl.create_default_context()
        email_message = MIMEMultipart()
        email_message["Subject"] = subject
        email_message["From"] = username
        email_message["To"] = receiver
    
        mime_text = MIMEText(msg, "html")
        email_message.attach(mime_text)
    
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.send_message(email_message)
