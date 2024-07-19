#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("16077282", default=None, cast=int)
API_HASH = config("de1f19d1abbaeada763cdbc22a055530", default=None)
BOT_TOKEN = config("6698534371:AAER-R5hc6bNBF60KO82LmwNkzqNelfVmHY", default=None)
SESSION = config("BAD1UeIAVD1jx0pfeRKpJE9_fdqPk4NncYfjfrQ2QGE2O5kHdP0TpijsBJUcQAcVuhfEm6aXx7YgIT0uvvWAe9jJGxuSSf2d0kUe1NIbAJd9k6IgoXmAcvBk2EiRa4YBUNllw9GwLlunsLIXaNYzNcV12ht1I47zD471vGTHr_3TRiuAEO7Fdl9ADQFL8S-sIUCSRmJvo-H6Grqdg74hdpnrRC3VtmJbp1or1xP_CobVTKtTPdjDGvyjeJolzcFp-KvI8ePHOaifwAeKPw2Tr4F_XO0jJNwvssj0zLXAzcOPHjY51hgO_3gqdgUdF-TSyjk5ZPgJ4Q1F5MlXJ4XuCHMip5f40AAAAAFlRRRxAA", default=None)
FORCESUB = config("savingahhbot12", default=None)
AUTH = config("5993993329", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
