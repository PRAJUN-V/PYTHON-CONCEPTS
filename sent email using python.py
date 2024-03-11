import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your email credentials and details
sender_email = "prajun0604@gmail.com"
receiver_email = "receiver@yopmail.com"
password = "fgmx pzdh xnxz yojz" #app password which we can get from 2 step verification last part of the page
subject = "Subject of the email"
body = "for testing purpose"

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))

# Establish a connection to the SMTP server (in this case, Gmail)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Start the TLS encryption
    server.starttls()

    # Log in to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully.")
