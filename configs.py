from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27613077"))
    API_HASH = getenv("API_HASH", "19dccde5b307a489ec9ded3a8a558e34")
    BOT_TOKEN = getenv("BOT_TOKEN", "7036432178:AAE9anXZHVs39melEFMideNkjK9FNsxKmhQ")

config = Config()
