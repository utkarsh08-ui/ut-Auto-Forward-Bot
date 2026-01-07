from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "2f4c8516cba7efff84376c742dc32e04")
      API_ID = int(getenv("API_ID", "23826477"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8561911063:AAErnz7GpkETjXmYOL9tSCdIQyBxBmFgl6g")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002297572866:-1002446713400").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
