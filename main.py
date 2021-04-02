import telebot
import requests

# Courrier maim module
bot = telebot.TeleBot('TOKEN')
keybord = telebot.types.ReplyKeyboardMarkup(True)
keybord.row('Meteo', 'Exchange')

@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, 'Hello my friend, first choose what you want to know:', reply_markup=keybord)


@bot.message_handler(content_types=['text'])
def send_text(message):
##### Meteoinfo section #####
    api_key = "5579671874d601427fff2c746b4381ac"
    city = "Kiev"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

    request = requests.get(url)
    json = request.json()

    temp = json.get("main").get("temp")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    long = json.get("coord").get("lon") # долгота
    lat = json.get("coord").get("lat") # широта
    city = json.get("name")
##### Exchange section #####
    url_ex = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    request_ex = requests.get(url_ex)


    if message.text.lower() == 'meteo':
        bot.send_message(message.chat.id, "Температура за окном {}".format(temp) + " градусов" + "\n"
                         "Минимальная температура сегодня {}".format(temp_min) + " градусов" + "\n"
                         "Максимальная температура сегодня {}".format(temp_max)  + " градусов" + "\n"
                         "Долгота {}".format(long) + ", широта {}".format(lat) + "\n"
                         "Город {}".format(city)
                         )
    elif message.text.lower() == 'exchange':
        bot.send_message(message.chat.id, 'В разработке')


bot.polling()


