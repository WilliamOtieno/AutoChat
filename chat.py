from twilio.rest import Client
from secrets import *


client = Client(account_sid, auth_token)


def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='This is for testing purposes''\nHello',
        to='whatsapp:+254719383956'
    )
    print(message.sid)
