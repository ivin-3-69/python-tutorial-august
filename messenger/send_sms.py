 
from twilio.rest import Client
from credentials import *

client = Client(account_sid, auth_token)
new_message = "more power baby"

message = client.messages.create( body=new_message,from_=my_twilio,to=my_cell)