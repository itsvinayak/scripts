from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC39b5b095c96c9df86b863b7028c87d0a'
auth_token = '6ae40fec41515881f881f510f21da6be'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Quweryyiitggh",
                     from_='+12564809031',
                     to='+918077564130'
                 )

print(message.sid)
