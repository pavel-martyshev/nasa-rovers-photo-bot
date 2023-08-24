import os

import dotenv
import redis
from aiogram import Bot

from keyboard.keyboard import InlineKeyboard
from messages.messages import Messages

keyboard = InlineKeyboard
messages = Messages
storage = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, '..', 'config.env')
dotenv.load_dotenv(CONFIG_PATH)

bot = Bot(os.getenv('TOKEN'))
