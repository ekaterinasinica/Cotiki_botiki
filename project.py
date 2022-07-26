# one = ['image/149785671459477acae2cdf1.42649864.jpg']
# two = ['image/animals_372.jpg']
# three = ['image/png-clipart-cat-kitten-scape-cats-mammal-animals.png']
# four = ['image/png-clipart-fat-orange-cat-orange-cat-kitty.png']
# five = [']image/red-or-white-cat-on-white-studio-background.jpg']
# six = ['image/the-gold-bengal-cat-on-white-space.jpg']
from unittest.mock import call

import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('5472211712:AAFx6eP3F7Bq9v15_zeRUFwofMA1tKeDiYA')



one = ['image/149785671459477acae2cdf1.42649864.jpg']
two = ['image/animals_372.jpg']
three = ['image/png-clipart-cat-kitten-scape-cats-mammal-animals.png']
four = ['image/png-clipart-fat-orange-cat-orange-cat-kitty.png']
five = [']image/red-or-white-cat-on-white-studio-background.jpg']
six = ['image/the-gold-bengal-cat-on-white-space.jpg']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, полюбуемся на котиков?")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_one = types.InlineKeyboardButton(text='1', callback_data='im')
        # И добавляем кнопку на экран
        keyboard.add(key_one)

        bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def start(message):
  photo = open('image/' + random.choice(os.listdir('image')), 'rb')
  bot.send_photo(message.from_user.id, photo)


bot.polling(none_stop=True, interval=0)


