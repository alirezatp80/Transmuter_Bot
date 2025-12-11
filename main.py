import telebot
import os
from dotenv import load_dotenv
from telebot.types import Message

#load token and use
load_dotenv()
TOKEN = os.getenv('API_TOKEN')

#CREATE BOT API
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler('start')
def say_hi(message : Message):
    bot.reply_to(message , 'Hi 👋 welcome to Transmuter ✨ \nHere you can perform any conversion you want 🔄')
    
    
bot.polling(
    skip_pending=True,
)

