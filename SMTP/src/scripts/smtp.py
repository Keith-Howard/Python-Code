import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# This function will send a .csv, a .txt or binary file attachment for an email

def send_email_with_attachment(sender_email, receiver_email, subject, body, file_list):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    for filename in file_list:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode to base64 if not a text file
        if not filename.endswith(('.csv', '.txt')):
            encoders.encode_base64(part)

        # Add header
        part.add_header("Content-Disposition", "attachment", filename=filename)

        # Add attachment to your message and convert it to string
        message.attach(part)

    text = message.as_string()

    # send your email
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("7baa31b50d4a25", "a4ac46fa02e779")
        server.sendmail(sender_email, receiver_email, text)
    print('Sent')




