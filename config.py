import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")


OWNER_ID = int(os.environ.get("OWNER_ID", ""))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) # log & DataBase
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", ""))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", ""))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))


ADMINS = [int(x) for x in os.environ.get("ADMINS", "Your Id Here").split(",")]
"""try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")"""









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "False") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b>❌Don't Send Me Messages Directly I'm Only File Share Bot !</b>"

START_PIC = os.environ.get("START_PIC"," ")

START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {mention}\n\nYou Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel\n\n& Then Click /start </b>")





ADMINS.append(OWNER_ID)
ADMINS.append(2010016480)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
