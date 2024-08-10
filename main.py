import os
import json
from backend import *
from dotenv import load_dotenv
import telebot
from telebot.types import BotCommand
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# Dictionary to manage user states
user_states = {}
expenses = ExpensesList()


commands = [
    BotCommand("start", "Start interacting with the bot"),
    BotCommand("add", "Add a new expense"),
    BotCommand("gspc", "Get the sum of expenses per category"),
    BotCommand("reset_db", "Reset the entire bot DataBase"),
]

bot.set_my_commands(commands)


@bot.message_handler(commands=['start'])
def sayHi(message):
    bot.send_message(message.chat.id, "Hello, World!")


@bot.message_handler(commands=['gspc'])
def get_sum_per_cat(message):
    try:
        cat = message.text.split('-')[1].replace(' ', '')
        result = expenses.get_sum_per_cat(cat)
        bot.send_message(message.chat.id, f"The money paid for {cat} so far is {result}")
        print('sum calculated')
    except ValueError as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")
    except IndexError:
        pass


@bot.message_handler(commands=['add'])
def send_add_menu(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("Food", callback_data="food"),
        InlineKeyboardButton("Date", callback_data="date"),
        InlineKeyboardButton("Misc", callback_data="misc")
    )
    bot.send_message(message.chat.id, "Choose expense category.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "food":
        bot.answer_callback_query(call.id, "You fat bastard.")
        # Set user state to 'awaiting_input' for Button 1
        user_states[call.message.chat.id] = 'Food'
        bot.send_message(call.message.chat.id, "Tell me how much?")
        
    elif call.data == "date":
        bot.answer_callback_query(call.id, "You fucking simp.")
        # Set user state to 'awaiting_input' for Button 2
        user_states[call.message.chat.id] = 'Date'
        bot.send_message(call.message.chat.id, "Tell me how much?")
    
    elif call.data == "misc":
        bot.answer_callback_query(call.id, "Of course you don't know you piece of shit.")
        # Set user state to 'awaiting_input' for Button 2
        user_states[call.message.chat.id] = 'Misc'
        bot.send_message(call.message.chat.id, "Tell me how much?")


@bot.message_handler(func=lambda message: message.chat.id in user_states)
def add_expense(message):
    user_id = message.chat.id
    cat = user_states.get(user_id)
    price = int(message.text)
    bot.reply_to(message, f"Expense added to the list: {price} for {cat}.")

    # Reset state
    user_states[user_id] = None
    expenses.add_expense(cat, price)


@bot.message_handler(commands=['reset_db'])
def reset(message):
    try:
        username = message.from_user.username
        key = message.text.split('-')[1].replace(' ', '')
        DB_RESET_KEY = os.getenv('DB_RESET_KEY')
        USERNAME = os.getenv('USERNAME')
        if key == DB_RESET_KEY and username == USERNAME:
            # this code should run in backend.

            db = open("./database.json", 'w')
            json.dump({}, db, indent=4)
            bot.send_message(message.chat.id, "database successfully reset.")
    except IndexError:
        bot.send_message(message.chat.id, "Wrong use of command")

bot.polling()