#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29434441
API_HASH = "5cfd6614a8968694050c1e2fdd3c05ad"
BOT_TOKEN = "6429688994:AAGJ_veDA_N6cepKD1vh2iUqEFwQiRyaCcc"
SESSION = "BQBFudqDWjzYQUkT0gKA27TVnCbpBQkxR9qaNgWnxls5L1jsE-le5Fz_r770vprxX0TAx_Z528LMAU_2zTnICrzc63b1iCQ04XCb7AdgS2BoXmWtPwGFKcW-CNbmJ1FTsBN8fLnms0g7LLrfNY0mquU3Vszq3mNRAode1HTGQ-Fb5csJqhjgLmC1p965MT2Wrxb9TqvzYm6Ge9ZsWo8eSSQ8cpqIgurrKxTQTWQYZO4yvHhNo6ZdVlTHWFPRl6KKer51_RFGXwnVHFC-Ll5JsBIN7CEbgUuAwbUH3HkVK8A4JEH2nqjyHfoh5PZey-NpH1aSDUw8koB-YSBCglIRD2GqSDTF5QA"
FORCESUB = "batchingupdate"
AUTH = 1211418085

auth = config("AUTH", default=None, cast=int)
ids = auth.split(",")
for id in ids:
    AUTH.append(int(id))
    
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
