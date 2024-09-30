import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os

load_dotenv()
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = os.getenv('mail_id')
password = os.getenv('mail_password')
sender_email = username 
receiver_email = input('Enter the Receiver Mail id: ')
subject = input('Enter the subject: ')
body = input('Enter the Body of the mail: ')

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))


image_path = input("Enter the Image path (leave blank if not applicable): ")
if image_path:
    try:
        with open(image_path, 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(image_path)}"')
            msg.attach(img)
    except Exception as e:
        print(f'Failed to attach image: {str(e)}')


pdf_path = input("Enter the PDF file path (leave blank if not applicable): ")
if pdf_path:
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf = MIMEApplication(pdf_file.read(), _subtype="pdf")
            pdf.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(pdf_path)}"')
            msg.attach(pdf)
    except Exception as e:
        print(f'Failed to attach PDF: {str(e)}')


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        print('Email sent successfully')
except Exception as e:
    print(f'Failed to send: {str(e)}')
