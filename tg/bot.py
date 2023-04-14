import telebot
from telebot import types
import model
from tg import qr_generator

bot = telebot.TeleBot('6223773161:AAH7f98O6qqqvag65vUlVx6QBS6JwGtjP9M')
@bot.message_handler(content_types=['text'], commands=['start'])
def HelloMessage(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    serv = types.KeyboardButton(text='Добавить сотрудника')
    keyboard.add(serv)
    welcome_message = bot.send_message(message.chat.id, "Добро пожаловать в систему учета рабочего времени!", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def emploee_adding(message):
    if message.text == "Добавить сотрудника":
        ask_fio = bot.send_message(message.chat.id, "Введите ФИО сотрудника, должность и номер телефона через пробел")
        bot.register_next_step_handler(ask_fio, getData)


def getData(message):
    data = message.text.split(" ")
    print(data)
    name = " ".join(data[0:3])

    model.user_add(name, data[3], data[4])
    qr_info = model.search_emploee(name)
    qr_generator.generateQr(qr_info[0][0], data[0])
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    serv = types.KeyboardButton(text='Добавить сотрудника')
    keyboard.add(serv)
    photo = open('/Users/vladislavcehov/PycharmProjects/qr_time/tg/test1.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, f"Сотрудник {name}", reply_markup=keyboard)
bot.polling()