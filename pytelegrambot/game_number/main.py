# import telebot
# from telebot import types
# import random

# token = '5941512711:AAGNnkuDUkXxocODo9uSOR1u0B8l07gdv9A'

# bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Bot started')
#     bot.send_message(message.chat.id, 'Введите своё ФИО:')
#     bot.register_next_step_handler(message, answer_user)

# def answer_user(message): #message.text == 'hi!'
#     bot.send_message(message.chat.id, f'Здравствуйте, {message.text}')
#     bot.send_message(message.chat.id, 'Test bot!')

# bot.polling()

import telebot
from telebot import types
import random

token = '5941512711:AAGNnkuDUkXxocODo9uSOR1u0B8l07gdv9A'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Играть')
button2 = types.KeyboardButton('Нет')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, начнём игру?', reply_markup=keyboard)
    bot.register_next_step_handler(message2, check_answer)


def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ок, тогда вот правила: нужно угадать число от 1 до 10 за 3 попытки')
        number = random.choice(range(1, 11))
        print(number)
        game(message, 3, number)
    else:
        bot.send_message(message.chat.id, 'Хорошо, пока!')



def game(message, attempts, number):
    message2 = bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message2, check_number, attempts-1, number)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Поздравляю! Вы выиграли!')
        start_message(message)
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Сорри, у тебя закончились попытки')
        start_message(message)
    else:
        bot.send_message(message.chat.id, f'Не верно! У тебя осталось: {attempts} попыток, попробуй ещё раз ввести число')
        game(message, attempts, number)


bot.polling()