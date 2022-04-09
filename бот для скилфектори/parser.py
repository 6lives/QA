import requests
from creds import api
import csv

def get_coin_list(api):
    url = f'https://min-api.cryptocompare.com/data/blockchain/list?api_key={api}'

    response = requests.get(url).json()
    with open('coin_list.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')

        for coin_name in response['Data'].keys():
            writer.writerow([coin_name])


def get_pair(api, base, quote, amount=1):
    url = f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}&api_key={api}'
    quote = quote.upper()

    response = requests.get(url).json()

    if response.get('Response') == 'Error':
        return 'Некорректный ввод. Ошибка имен валютных пар'

    price = response.get(f'{quote}')
    return f'При обмене вы получите: {str(round((price * float(amount)), 4)) + quote}'


#get_pair(api, 'BTC', 'USD')
