import json
import requests
from config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'не удалось обработать валюту "{quote}"')

        try:
            quote_ticker = keys[base]
        except KeyError:
            raise APIException(f'не удалось обработать валюту "{base}"')
        if quote == base:
            raise APIException("Вы ввели одинаковые валюты.\nПовторите запрос.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}"')
        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        totalbase = json.loads(r.content)[keys[base]]
        next_price = totalbase*amount
        last_price = round(next_price, 3)
        return last_price