from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "88cf2c17c7a2bd21f4204c89c648dd40")
      API_ID = int(getenv("API_ID", "25848289"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6907596900:AAF-GGlBBcm1WWAF1ekm-nYcO1jwq-oV_H0")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002045685365:-1002140930815").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
