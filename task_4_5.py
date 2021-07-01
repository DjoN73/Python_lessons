from requests import get, utils
from datetime import date
from sys import argv


def currency_rates(code):
    responce = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
    content = responce.split('<Valute ID=')
    d, m, y = content[0].split()[3].split('Date=')[1][1:-1].split('.')
    for el in content:
        if code.upper() in el:
            print(date(year=int(y), month=int(m), day=int(d)))
            return float(el.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    valute = argv[1]
    print(currency_rates(valute))
