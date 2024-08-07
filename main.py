import os
from dotenv import load_dotenv
import telebot

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def sayHi(message):
    bot.send_message(message.chat.id, 'Hello, World!')

bot.polling()