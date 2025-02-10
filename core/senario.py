import telebot
import os
from telebot import *

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

user_info = {}

list_btn = ['Back']

@bot.message_handler(commands=['start'])
def Start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    start_btn1 = types.KeyboardButton('Courses')
    start_btn2 = types.KeyboardButton('Back')
    start_btn3 = types.KeyboardButton('Information')
    markup.add(start_btn1 , start_btn2 , start_btn3)
    bot.reply_to(message , 'Choose one of the options below.' , reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Information')
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for info in list_btn:
        markup.add(types.KeyboardButton(info))
    bot.reply_to(message, 'در صورت نیاز با این شماره\n**08612345**\n   تماس بگیرید', reply_markup=markup)
    
def courses(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=4)
    for courses in list_btn:
        markup.add(types.KeyboardButton(courses))
        btn1 = types.KeyboardButton('Spring')
        btn2 = types.KeyboardButton('Summer')
        btn3 = types.KeyboardButton('Autumn')
        btn4 = types.KeyboardButton('Winter')
    markup.add(btn1 , btn2 , btn3 , btn4)
    bot.reply_to(message , 'Choose a season' , reply_markup=markup)
    bot.register_next_step_handler(message , btn)


def Spring_btn(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('ccna' , callback_data='ccna')
    b2 = types.InlineKeyboardButton('lpic' , callback_data='btn1')
    b3 = types.InlineKeyboardButton('net+' , callback_data='btn1')
    markup.add(b1 , b2 , b3)
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)
def Summer_btn(message):
    markup = types.InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton('django' , callback_data='django')
    a2 = types.InlineKeyboardButton('python' , callback_data='python')
    a3 = types.InlineKeyboardButton('icdl' , callback_data='icdl')
    a4 = types.InlineKeyboardButton('ccna' , callback_data='ccna')
    markup.add(a1 , a2 , a3)
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)

def Autumn_btn(message):
    markup = types.InlineKeyboardMarkup()
    A1 = types.InlineKeyboardButton('django_DRF' , callback_data='django_DRF')
    A2 = types.InlineKeyboardButton('lpic2' , callback_data='lpic2')
    A3 = types.InlineKeyboardButton('mcsa' , callback_data='mcsa')
    markup.add(A1 , A2 , A3)
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)

def Winter_btn(message):
    markup = types.InlineKeyboardMarkup()
    w1 = types.InlineKeyboardButton('django_DevOps' , callback_data='django_DevOps')
    w2 = types.InlineKeyboardButton('mcsp' , callback_data='mcsp')
    w3 = types.InlineKeyboardButton('network' , callback_data='network')
    markup.add(w1 , w2)
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)



@bot.callback_query_handler(func=lambda call: True)
def handle_regester_course(call):
    message = call.message
    user_info['course'] = call.data
    message = call.message
    bot.reply_to(message , 'Start registration')
    bot.reply_to(message , 'نام و نام خانوادگی خود را وارد کنید')
    bot.register_next_step_handler(message , phone) 
def phone(message):
    bot.reply_to(message , 'شماره تلفن همراه خود را وارد کنید')
    user_info['name'] = message.text
    bot.register_next_step_handler(message , finish)
def finish(message):
    bot.reply_to(message , 'پیش ثبت نام شما با موفقیت انجام شد')
    user_info['finish'] = message.text
    with open("./info.txt" , "a") as file:
        for key in user_info:
            file.write(user_info[key]+'\n')
        file.write('--------------------')
        file.write('\n')

@bot.message_handler(func=lambda message: True)
def btn(message):
    if message.text == 'Back':
        Start_message(message)
    elif message.text == 'Information':
        info(message)
    elif message.text == 'Courses':
        courses(message)
    elif message.text == "Spring":
        # user_info["season"] = message.text
        Spring_btn(message)
    elif message.text == 'Summer':
        # user_info["season"] = message.text
        Summer_btn(message)
    elif message.text == "Autumn":
        # user_info["season"] = message.text
        Autumn_btn(message)
    elif message.text == "Winter":
        # user_info["season"] = message.text
        Winter_btn(message)





bot.infinity_polling()