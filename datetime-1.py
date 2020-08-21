import datetime
import pytz

now = datetime.datetime.now().astimezone(pytz.timezone("hongkong"))


print(now.strftime('%B-%d, %Y'))
now = now.strptime( now.strftime('%B-%d, %Y') ,"%B-%d, %Y")
print(now)
now_object = repr(now) 
print(now_object)