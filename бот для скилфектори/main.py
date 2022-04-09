import telebot
from creds import token, api
from keyboards import start_buttons
from parser import get_coin_list, get_pair


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, 'Бот позволяет узнать о курсе валют', reply_markup = start_buttons())


@bot.message_handler(func= lambda message: message.text == 'List')
def money_list(message):

    '''функция отлавливает из чата слово List и выполняет команду на выдачу csv
    со списком доступных коинов'''

    bot.send_message(message.chat.id, 'Можете скачать список доступных коинов')
    get_coin_list(api)
    with open('coin_list.csv', 'rb') as file:
        bot.send_document(message.chat.id, document=file)

@bot.message_handler(func= lambda message: message.text == 'Search')
def pair_search(message):

    '''функция отлавливает из чата слово Search и запрашивает у юзера
    текст для поиска валют, который автоматически будет отловлен и будет
    выполнена функция pair_check'''

    bot.send_message(message.chat.id, 'Введите через пробел валюту 1, валюту 2, количество валюты 1 \nК примеру: btc usd 100')
    bot.register_next_step_handler(message, pair_check)

def pair_check(message):

    '''функция получает данные от юзера, фильтрует их и совершает запрос на
    их основании '''

    try:
        user_input = message.text.replace(',' , '.').split()
        if not len(user_input) == 3:
            raise ValueError
        coin1, coin2, amount = user_input
        print(amount)
        bot.send_message(message.chat.id, f'{get_pair(api, coin1, coin2, amount)}')
        start(message)
    except ValueError as e:
        bot.send_message(message.chat.id, 'Некорректный ввод. Сверьтесь с шаблоном запроса')
        start(message)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Что то пошло не так, попробуйте снова')
        start(message)


if __name__ == '__main__':
    bot.infinity_polling()
