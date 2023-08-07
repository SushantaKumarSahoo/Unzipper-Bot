# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("23573562"))
    API_HASH = os.environ.get("90c3fcac22ac68a5e78d4804942603f4")
    BOT_TOKEN = os.environ.get("6024068299:AAEAAxAyrRaDmOLfqM23wmyliRq3fbDgX6o")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL"))
    BOT_OWNER = int(os.environ.get("5145748626"))
    MONGODB_URL = os.environ.get("mongodb+srv://sksahoo153315:<Sa!Tg7vv1533>@cluster0.kqdabs0.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("bEqPXWFPKDIxRFK2xs6kraxOYQuV8jjj")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
