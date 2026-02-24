import smtplib
from email.message import EmailMessage

def send_mail(sender, app_password, receiver, subject, body):

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        print("Connecting to server...")
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        print("Logging in...")
        smtp.login(sender, app_password)

        print("Sending mail...")
        smtp.send_message(msg)

        smtp.quit()
        print("Mail sent successfully.")

    except:
        print("Error while sending mail")

def main():
    sender_email = input("Sender email: ")
    app_password = input("App password: ")
    receiver_email = input("Receiver email: ")

    subject = "Testing Mail"
    body = "Hello,\nTanmay Thorat This Side\nThanks for reading!"

    send_mail(sender_email, app_password, receiver_email, subject, body)

if __name__ == "__main__":
    main()