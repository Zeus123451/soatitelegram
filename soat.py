from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = 1070048 #my.telegram.org dan olgan apiidni qoying
api_hash = "d2c092dcc7d25a9e704cf4f11f0f58b0" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x),
    about="O'zbekistonda soat: " +str(x)
    ))
    time.sleep(30)
