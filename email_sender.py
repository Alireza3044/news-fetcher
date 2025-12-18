import smtplib, ssl
from email.message import EmailMessage

def send_email(title, message):
    host = "smtp.gmail.com"
    port = 465

    username = "alireza1384928@gmail.com"
    password = "desa lbme advj ossz"

    receiver = "alireza1384928+news@gmail.com"
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg["Subject"] = title
    msg["From"] = username
    msg["To"] = receiver
    msg.set_content(message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)
