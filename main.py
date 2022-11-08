import os
import telebot
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.reply_to(message,'Aur bhau ka ba?')

@bot.message_handler(commands=['hello'])
def hello(message):
    name = message.from_user.first_name
    msg = f'Hello {name}'
    bot.send_message(message.chat.id,msg)

@bot.message_handler(commands=['joke'])
def send_joke(message):
    response = requests.get('https://v2.jokeapi.dev/joke/Dark,Programming,Miscellaneous,Pun,Spooky?')
    res = response.json()
    if(res['type'] == 'single'):
        msg = res['joke']
    else:
       msg =f"Setup-> {res['setup']} \nDelivery->{res['delivery']}"

    bot.send_message(message.chat.id,msg)

@bot.message_handler(commands=['meme'])
def send_meme(message):
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    res = response.json()
    bot.send_photo(message.chat.id,res['url'])
    

bot.infinity_polling()