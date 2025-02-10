import telebot
import os
from telebot import *

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

user_info = {}


list_btn = ['Back']
list_Season = {
    'Spring': ['ccna' , 'lpic' , 'django', "icdl"],
    'Summer': ['mcsa' , 'ccnp'],
    'Autumn': ['python' , 'photoshop' , 'C#'],
    'Winter': ['django2' , 'python' ' net +'],
}


@bot.message_handler(commands=['start'])
def Start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    start_btn1 = types.KeyboardButton('Courses')
    start_btn2 = types.KeyboardButton('Back')
    start_btn3 = types.KeyboardButton('Information')
    markup.add(start_btn1 , start_btn2 , start_btn3)
    bot.reply_to(message , 'Choose one of the options below.' , reply_markup=markup)
    user_info = {}


@bot.message_handler(commands=['Information'])
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
    bot.reply_to(message , 'School contact number')
    for info in list_btn:
        markup.add(types.KeyboardButton(info))
    bot.reply_to(message , 'در صورت نیاز با این شماره\n**08612345**\n   تماس بگیرید' , reply_markup=markup)

def courses(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=4)
    bot.reply_to(message , 'Choose one of the options below.')
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
    for cour in list_Season['Spering']:
        markup.add(types.InlineKeyboardButton(cour , callback_data=cour))
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)

def Summer_btn(message):
    markup = types.InlineKeyboardMarkup()
    for cour in list_Season['Summer']:
        markup.add(types.InlineKeyboardButton(cour , callback_data=cour))
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)

def Autumn_btn(message):
    markup = types.InlineKeyboardMarkup()
    for cour in list_Season['Autumn']:
        markup.add(types.InlineKeyboardButton(cour , callback_data=cour))
    bot.reply_to(message , 'Please fill out the registration form below.' , reply_markup = markup)

def Winter_btn(message):
    markup = types.InlineKeyboardMarkup()
    for cour in list_Season['Winter']:
        markup.add(types.InlineKeyboardButton(cour , callback_data=cour))
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
        Spring_btn(message)
    elif message.text == 'Summer':
        Summer_btn(message)
    elif message.text == "Autumn":
        Autumn_btn(message)
    elif message.text == "Winter":
        Winter_btn(message)





bot.infinity_polling()