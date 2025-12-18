import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject: str, msg: str) -> None:
    host = "smtp.gmail.com"
    port = 465

    username = "alireza1384928@gmail.com"
    password = "desa lbme advj ossz"

    receiver = "alireza1384928+news@gmail.com"
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
