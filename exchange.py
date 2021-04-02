import telebot

bot = telebot.TeleBot('1702630099:AAHdLHcgDnoSPxODXZt9x15Hta0mugxPtdM')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет',)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()

