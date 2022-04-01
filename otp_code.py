from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5efb90c8a38575e08124a2f16846c05b"
# Your Auth Token from twilio.com/console
auth_token  = "c5cbf6b329d5021f61c6448ca77d78ae"

client = Client(account_sid, auth_token)

#generate OTP
import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Your OTP:", totp.now())

#Sending SMS 
message = client.messages.create(
    to="+919698605200",
    from_="+18438897559",
    body=totp.now())

print(message.sid)