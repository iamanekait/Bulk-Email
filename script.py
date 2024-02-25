import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Prompt user to input sender's email address
sender_address = input("Enter your email address: ")
password = input("Enter your email password: ")  # Prompt user for the password

# Read email addresses from Excel
try:
    emails_df = pd.read_excel("Email.xlsx")
    emails = emails_df['Emails'].tolist()
except FileNotFoundError:
    print("Email.xlsx file not found.")
    exit()

# Prompt user for subject, message, and attachment path
subject = input("Enter the email subject: ")
message = input("Enter the email message: ")
attachment_path = input("Enter the path of the attachment (if any), or press Enter to skip: ")

# SMTP server setup
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_address, password)
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate. Please check your email and password.")
    exit()
except Exception as e:
    print("An error occurred:", e)
    exit()

# Send emails
for recipient_email in emails:
    msg = MIMEMultipart()
    msg['From'] = sender_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if attachment_path:
        if os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)
        else:
            print(f"Attachment file '{attachment_path}' not found. Skipping attachment for {recipient_email}")

    try:
        server.sendmail(sender_address, recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")

# Quit server
server.quit()
