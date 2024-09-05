# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID",21254911))
    API_HASH = os.environ.get("API_HASH","95e927b3c48ac0af4ebb1c3ffeb0069b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7461358634:AAHqk9o56O33T6uy8h4rWFFs_GmNwlhzZXc")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL",-1002243837012))
        
    MONGODB_URL = os.environ.get("MONGODB_URL","mongodb+srv://JXXS7:JXXS7@cluster0.xxkw0.mongodb.net/?retryWrites=true&w=majority")
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", "Unzipper_Bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER",6169288210))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
