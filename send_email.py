import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    sender = "anudeepsurya111@gmail.com"
    password = "vwxxjztpfvvhanyt"
    receiver = "anudeepsurya111@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)