import os
import telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.reply_to(message,'Aur bhau ka ba?')

bot.polling()