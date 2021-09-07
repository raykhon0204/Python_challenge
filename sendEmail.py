import smtplib
EMAIL = 'raykhon.juraeva@gmail.com'
PASSWORD = 'Esmira2015!'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, receiver_email, message)
send_email('raykhon2013@gmail.com', "Test", 'I sent an email.')