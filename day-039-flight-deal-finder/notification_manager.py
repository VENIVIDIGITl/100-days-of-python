from twilio.rest import Client

TWILIO_ACCOUNT_SID = ''     # Your Twilio account sid
TWILIO_AUTH_TOKEN = ''      # Your Twilio account auth token
TWILIO_NUMBER = ''          # Your Twilio number
RECIPIENT_NUMBER = ''       # Your number (verified with twilio)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=RECIPIENT_NUMBER,
        )

        print(message.status)
