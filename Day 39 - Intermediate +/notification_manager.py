from twilio.rest import Client

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = YOUR_ACCOUNT_SID
        self.auth_token = YOUR_AUTH_TOKEN

    def send_sms(self, data):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=f"\nLow Price Alert! Only £{data.price} to fly "
                 f"from {data.origin_city}-{data.origin_airport} to "
                 f"{data.destination_city}-{data.destination_airport}, "
                 f"from {data.out_date} to {data.return_date}.",
            from_=YOUR_TWILIO_PHONE_NUMBER,
            to=YOU_REAL_NUMBER
        )
        print(f"Message SID: {message.sid}")
