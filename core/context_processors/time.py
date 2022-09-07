import datetime
import locale
import requests


def current_time(request):
    """
    Функция, получающая текущую дату с сервера
    и возвращающая ее в переменной 'current_time'
    """
    response = requests.post('https://api.taxideli.ru/test/gettime')
    time_data = response.json()['dataAns']

    locale.setlocale(locale.LC_ALL, "ru_RU")

    time = datetime.datetime.fromtimestamp(time_data/1000.0)
    current_time = time.strftime('%a, %d.%m.%Y %H:%M')

    return {
        'current_time': current_time
    }
