#!/usr/bin/env python
import requests
import random
import telebot
import pickle
from telebot import types
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# f = open(r'users.pkl', 'rb')
# print(f)
# try:
#     users = pickle.load(f)
# except:
#     users = set()
# f.close()

stickers = ['CAADAgADuAADV08VCIU2WpK6h9FGAg', 'CAADAgADuQADV08VCPlvmfT9JAFFAg', 'CAADBAADOgEAAmuuXgmasYVZ3o9jeQI', 'CAADBAADEQEAAmuuXgmu2srN3lZnKgI', 'CAADAgADDgUAAnwFBxskRdrPGP8flwI', 'CAADAgADAgADaCpFIZ_Gk9Ci9_u_Ag']

users = {}

class User:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.age = None
        self.sex = None

TOKEN = '880951017:AAGnnIXaKShR8umg7FhOcXhj4TPl4yu-FhI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    user = User(message.from_user.id)
    users[message.from_user.id] = user
    user.name = message.from_user.first_name + " " + message.from_user.last_name
    bot.send_message(message.chat.id, f"Привет, я бот! Тебя зовут \n{message.from_user.first_name} {message.from_user.last_name}?", reply_markup=gen_name_markup())


def gen_name_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Да, всё верно", callback_data="cb_yes"), InlineKeyboardButton("Нет", callback_data="cb_no"))
    return markup


def name_input(message: Message):
    # print(call.message)
    #  = message.from_user.id
    user = users[message.from_user.id]
    user.name = message.text
    bot.send_sticker(message.chat.id, random.choice(stickers))
    bot.send_message(message.chat.id, f'Отлично, {user.name}, вот тебе стикер')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user = users[call.from_user.id]
    if call.data == "cb_yes":
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id, reply_markup = None)
        bot.send_sticker(call.message.chat.id, random.choice(stickers))
        bot.send_message(call.message.chat.id, f'{user.name}, вот тебе стикер. Пиши что-нибудь, пришлю ещё')

    elif call.data == "cb_no":
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id, reply_markup = None)
        bot.send_message(call.message.chat.id, "Тогда введите ваше полное имя")
        bot.register_next_step_handler(call.message, name_input)


@bot.message_handler(content_types=['text'])
def color_choice(message: Message):
    print(message)
    try:
        user = users[message.from_user.id]
        bot.send_sticker(message.chat.id, random.choice(stickers))
        bot.send_message(message.chat.id, f'{user.name}, вот тебе ЕЩЕ стикер')
    except:
        send_welcome(message)
# # print()
#
#
# def gen_markup():
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn_black = types.KeyboardButton('Чёрный') #, callback_data=f"cb_black")
#     btn_white = types.KeyboardButton('Белый') #, callback_data=f"cb_white")
#     btn_yellow = types.KeyboardButton('Желтый') #, callback_data=f"cb_yellow")
#     markup.row(btn_black, btn_white, btn_yellow)
#     return markup
#
#
# def process_sex_step(message):
#     chat_id = message.chat.id
#     sex = message.text
#     if (sex == u'Чёрный') or (sex == u'Белый') or (sex ==u'Желтый'):
#         bot.send_message(chat_id, f"Nice to meet you, {sex}")
#     else:
#         raise Exception()
#
#
# @bot.message_handler(content_types=['text'])
# def msg_handler(message: Message):
#     reply = ""
#     if message.from_user.id in users:
#         reply += f"Ты мне уже писал. "
#     else:
#         reply += "Ты мне еще не писал. "
#     users.add(message.from_user.id)
#     # bot.send_message(message.chat.id, f'{reply}{message.from_user.first_name}, ты зачем мне шлешь "{message.text}"? Лучше стикер пришли')
#     f = open(r'users.pkl', 'wb')
#     pickle.dump(users, f)
#     f.close()
#     # reply_markup = gen_markup()
#     bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())
#     process_sex_step(message)
#
#
# @bot.message_handler(content_types=['sticker'])
# def sticker_handler(message: Message):
#     bot.send_sticker(message.chat.id, random.choice(stickers))
#     bot.send_message(message.chat.id, f'Вот тебе тоже стикер. Шли еще')
#     print(message)
#     print(message.sticker)
#     # bot.reply_to(message, str(random.random()))
#
# @bot.inline_handler(lambda query: query.query == 'text')
# def query_text(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#         bot.answer_inline_query(inline_query.id, [r, r2])
#     except Exception as e:
#         print(e)
#
# @bot.message_handler(commands=['start', 'help'])
# def command_handler(message: Message):
#     bot.send_message(message.chat.id, f'Ты зачем мне шлешь команду "{message.text}" ')

# @bot.message_handler(content_types=['text'])
# def echo_digits(message: Message):
#     bot.reply_to(message, str(random.random()))


bot.polling(timeout=60)


# MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
# r = requests.get(f'{MAIN_URL}/getUpdates')
# print(r.json())
