# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "7236453")
    API_HASH = os.environ.get("API_HASH", "33010a70e94f80e55145980072cce969")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://videshi:videshi@videshi.wtffv.mongodb.net/?retryWrites=true&w=majority&appName=videshi")
    DB_NAME = os.environ.get("DB_NAME", "madflixbotz")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '7873618934').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
