import COVID19Py
import telebot

bot = telebot.TeleBot('2113113800:AAGRXLHCNcSwR_pHwU9k3jkGzORPmJ154TA')

covid = COVID19Py.COVID19()

latest = covid.getLatest()

@bot.message_handler(commands=['start'])
def start(message):
 
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"

    bot.send_message(message.chat.id, send_mess, parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'украина':
        location = covid.getLocationByCountryCode('UA')
    elif get_message_bot == 'россия':
        location = covid.getLocationByCountryCode('RU')
    else:
        location = covid.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболвшие: </b>{location['confirmed']}"
    if final_message == "":
        date = location[0]['last_updated'].split('|')
        time = date[0].split('.')
        final_message = f"<u>Данные по стране:</u>\nНасиление:::{location[0]['country_population']}\n"\
                        f"<u>Последнее обновление:</u><b>{date[0]}{time[0]}</b>\n"\
                        f"<u>Заболвших:</u><b>{location[0]['latest']['confirmed']}</b>\n"\
                        f"<u>Смерти:</u><b>{location[0]['latest']['deaths']}</b>"
    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
