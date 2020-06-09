from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
import random
api_id = 1070048 #my.telegram.org dan olgan apiidni qoying
api_hash = "d2c092dcc7d25a9e704cf4f11f0f58b0" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = 1
    length = 10
    number = int(number)
    length = int(length)
    for n in range(number):
        password =''
        for i in range(length):
          password += random.choice(chars)

app.start()
while True:
 
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x)+' '+str(password),
    about="O'zbekistonda soat: " +str(x)
    ))
    time.sleep(20)
