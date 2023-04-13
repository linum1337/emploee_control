import telebot
bot = telebot.TeleBot('6223773161:AAH7f98O6qqqvag65vUlVx6QBS6JwGtjP9M')
from stats import send_stat
@bot.message_handler(content_types=['text'], commands=['start'])
def HelloMessage(message):
    welcome_message = bot.send_message(message.chat.id, "Добро пожаловать в систему учета рабочего времени! Отправьте свое ФИО, номер телефона и должность")
    fio = bot.send_message(message.chat.id, "Укажите ФИО")
    bot.register_next_step_handler(fio, getUsername)

def getUsername(message):
    us = message.text
    print(us)
    phone = bot.send_message(message.chat.id, "Укажите номер телефона")
    bot.register_next_step_handler(phone, getPhoneNumber, us)

def getPhoneNumber(message, us):
    phone = message.text
    print(phone)
    role = bot.send_message(message.chat.id, "Укажите должность")
    bot.register_next_step_handler(role, getRole, us, phone)

def getRole(message, us, phone):
    role = message.text
    send_stat(us, phone, role)
    print(role)
bot.polling()