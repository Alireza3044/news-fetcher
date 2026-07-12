import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config

SERVER_HOST_NAME = config("SERVER_HOST_NAME")
SERVER_HOST_PORT = config("SERVER_HOST_PORT", cast=int)
SERVER_EMAIL_USERNAME = config("SERVER_EMAIL_USERNAME")
SERVER_EMAIL_PASSWORD = config("SERVER_EMAIL_PASSWORD")


def send_email(subject: str, msg: str, receiver: str) -> None:
    host = SERVER_HOST_NAME
    port = SERVER_HOST_PORT

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
