import telebot
import time
from telebot import types
import random

bot = telebot.TeleBot('5472211712:AAFx6eP3F7Bq9v15_zeRUFwofMA1tKeDiYA')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, полюбуемся на котиков?.")

bot.polling(none_stop=True, interval=0)
