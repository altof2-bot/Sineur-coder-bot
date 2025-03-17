from telethon import TelegramClient
from decouple import config
import logging
import os
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Basics
api_id = 24777493
api_hash = "bf5a6381d07f045af4faeb46d7de36e5"

try:
    bot_token = config("7914348044:AAFgLDck79PJWM-WU_z8DFMwW32QEuLsR5Q", default=None)
    mongo = config("mongodb+srv://altof2:123Bonjoure@cluster0.s1suq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
except Exception as e:
    logging.warning(e)
    exit(0)


data = []
download_dir = "downloads/"
if not os.path.isdir(download_dir):
    os.makedirs(download_dir)

try:
    mongo_db = AsyncIOMotorClient(mongo)
except Exception as e:
    logging.warning(e)
    exit(0)

bot_db = mongo_db["VideoEncoder"]

try:
    BotzHub = TelegramClient("BotzHub", api_id, api_hash).start(bot_token=bot_token)
except Exception as e:
    logging.info(f"Error\n{e}")
    exit(0)
