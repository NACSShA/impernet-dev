import telebot
from telebot import types

from config import TOKEN
from database import init_db

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

init_db()

print("IMPERNET запущен.")

bot.infinity_polling(skip_pending=True)
