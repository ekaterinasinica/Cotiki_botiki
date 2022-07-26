import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('5472211712:AAFx6eP3F7Bq9v15_zeRUFwofMA1tKeDiYA')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, полюбуемся на котиков?")
        keyboard = types.InlineKeyboardMarkup()
        key_one = types.InlineKeyboardButton(text='1', callback_data='im')
        keyboard.add(key_one)
        bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def start(message, keyboard=None):
    photo = open('image/' + random.choice(os.listdir('image')), 'rb')
    bot.send_photo(message.from_user.id, photo)
    keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
    key_one = types.InlineKeyboardButton(text='1', callback_data='im')
    # И добавляем кнопку на экран
    keyboard.add(key_one)
    bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
