import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.recipient = "+85511702696"
        self.p_line = "+18705282420"
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']

    def send_sms(self, body):
        content = "Price change detected"
        for i in body:
            content = content + \
                f"\n- {i['city']} drop from {i['prev_price']} to {i['lowestPrice']} "

        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=content,
            from_=self.p_line,
            to=self.recipient
        )
        return message.error_code
