# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28243586"))
    API_HASH = getenv("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = getenv("BOT_TOKEN", "7427875913:AAECLn_AjdTMSizPFEnHQPwm8G855Hi2EIY")
    FSUB = getenv("FSUB", "Cricketxutkarshfamily")
    CHID = int(getenv("CHID", "-1002020503341"))
    SUDO = list(map(int, getenv("SUDO", "5340652544 1844080002").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
