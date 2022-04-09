from telebot import types

def start_buttons():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itm1 = types.KeyboardButton('Search')
    itm2 = types.KeyboardButton('List')
    keyboard.row(itm1,itm2)


    return keyboard
