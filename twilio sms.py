from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number (bought or verified on Twilio)
twilio_phone_number = 'your_twilio_phone_number'

# The recipient's phone number
recipient_phone_number = 'recipient_phone_number'

# The message you want to send
message_body = 'Hello from Twilio! This is a test SMS message.'

try:
    # Send the SMS message
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("Message sent successfully!")
    print("Message SID:", message.sid)
except Exception as e:
    print("Failed to send message:", str(e))
