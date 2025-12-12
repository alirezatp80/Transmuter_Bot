import telebot
import os
from dotenv import load_dotenv
from telebot.types import Message , ReplyKeyboardMarkup , InlineKeyboardButton , InlineKeyboardMarkup
from text import help_unit , help_base , unit_page,base_page
from transmuter import define_calculate
from transmuter_base import define_calculate_base
from transmuter_date import Gregorian_date,Persian,Islamic


#load token and use
load_dotenv()
TOKEN = os.getenv('API_TOKEN')

#CREATE BOT API
bot = telebot.TeleBot(token=TOKEN)

#button for app
key_markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2 )
key_markup.add('Unit' , 'Base' , 'Date' , 'About')

date_btn = ReplyKeyboardMarkup(resize_keyboard=True)



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'unit_btn':
        bot.send_message(call.message.chat.id, f'{help_unit}' )
    elif call.data == 'base_btn':
        bot.send_message(call.message.chat.id , f'{help_base}') 


@bot.message_handler(commands='start')
def say_hi(message : Message):
    bot.reply_to(message , 'Hi 👋 Welcome to Transmuter ✨\nHere you can perform any conversion you like 🔄' , reply_markup = key_markup)
    

@bot.message_handler()
def convering(message:Message):
    if message.text == 'Unit':
        back_btn = ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn.add('Back')
        bot.send_message(message.chat.id , '🔄 You are now in Unit Conversion Mode', reply_markup=back_btn)
        help_for_unit = InlineKeyboardButton('help' , callback_data='unit_btn')
        markup_unit = InlineKeyboardMarkup().add(help_for_unit)
        bot.send_message(message.chat.id , f'{unit_page}',reply_markup=markup_unit)
       
        bot.register_next_step_handler(message , unit_func)
        
        
        
    elif message.text == "Base":
        back_btn = ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn.add('Back')
        bot.send_message(message.chat.id , '🔄 You are now in Base Conversion Mode', reply_markup=back_btn)
        help_for_base = InlineKeyboardButton('help' , callback_data='base_btn')
        markup_base = InlineKeyboardMarkup().add(help_for_base)
        
        bot.send_message(message.chat.id , f'{base_page}',reply_markup=markup_base)

        bot.register_next_step_handler(message , base_func)
        
        

    elif message.text == 'Date' :
        date_btn.add('Gregorian', 'Persian' , 'Islamic' , 'back')
        bot.send_message(message.chat.id , f'📅 Choose the input calendar' , reply_markup=date_btn)

    elif message.text == 'About' :
        bot.send_message(message.chat.id , f"""👋 Hi, I'm Alireza Tashani  
💻 Python Developer & Programmer  
📧 Email: alirezatd80@gmail.com
""")
    elif message.text == 'Gregorian':
        bot.send_message(message.chat.id , 'Enter Date Gregorian📅 :') 
        
        bot.register_next_step_handler(message , Gregorian_date_func)
        
    elif message.text == 'Persian':
        bot.send_message(message.chat.id , 'Enter Date Persian🌞 :') 
        
        bot.register_next_step_handler(message , Persian_date)
        
        
    elif message.text == 'Islamic':
        bot.send_message(message.chat.id , 'Enter Date Islamic🌙 :') 
        
        bot.register_next_step_handler(message , Islamic_date)
        
    elif message.text == 'back':
        bot.delete_message(message.chat.id , message.message_id)
        bot.send_message(message.chat.id , '📍 Main Menu' , reply_markup = key_markup)
    
    else:
        bot.send_message(message.chat.id , f'⚠️ Invalid input type.choose a button')


def unit_func(message : Message):
    if message.text == 'Back':
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(
                message.chat.id,
                '📍 Returned to main menu.',
                reply_markup=key_markup
            )
            return 
    else:
        result = define_calculate(message.text)
        bot.reply_to(message , result , reply_markup=key_markup)
def base_func(message : Message):
    if message.text == 'Back':
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(
                message.chat.id,
                '📍 Returned to main menu.',
                reply_markup=key_markup
            )
            return 
    else:
        
        result = define_calculate_base(message.text)
        bot.reply_to(message , result,reply_markup=key_markup)

def Gregorian_date_func(message : Message):
    if message.text == 'Back':
        bot.delete_message(message.chat.id , message.message_id)
        bot.send_message(
            message.chat.id,
            '📍 Returned to main menu.',
            reply_markup=key_markup
        )
        return
    else:
        result = Gregorian_date(message.text)
        bot.reply_to(message , result , reply_markup =date_btn )
        
        
def Persian_date(message : Message):
    if message.text == 'Back':
        bot.delete_message(message.chat.id , message.message_id)
        bot.send_message(
            message.chat.id,
            '📍 Returned to main menu.',
            reply_markup=key_markup
        )
        return
    else:
        result = Persian(message.text)
        bot.reply_to(message , result , reply_markup =date_btn )
def Islamic_date(message : Message):
    if message.text == 'Back':
        bot.delete_message(message.chat.id , message.message_id)
        bot.send_message(
            message.chat.id,
            '📍 Returned to main menu.',
            reply_markup=key_markup
        )
        return
    else:
        result = Islamic(message.text)
        bot.reply_to(message , result , reply_markup =date_btn )
        
      
bot.polling(
    skip_pending=True,
)

