import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jasmaljabbarghazali@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'qrso bjfb yeit mxjk'       # Your email password or App Password
DEFAULT_FROM_EMAIL = 'jasmaljabbarghazali@gmail.com'

# Function to send an email
def send_email(to_email, subject, body):
    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = DEFAULT_FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)  # Login to your email account

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server.quit()  # Close the connection

# Usage example
if __name__ == "__main__":
    recipient = 'abcdefg@yopmail.com'  # Replace with the recipient's email address
    subject = 'otp'
    body = 'otp: 234567'

    send_email(recipient, subject, body)
