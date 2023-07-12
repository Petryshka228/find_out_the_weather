import requests

TRANSLATION_WEATHER = {
    'Light rain': 'Небольшой дождь', 'Moderate rain': 'Умеренный дождь', 'Light rain shower': 'Легкий дождь',
    'Partly cloudy': 'Переменная облачность', 'Patchy rain possible': 'Возможен кратковременный дождь',
    'Light drizzle': 'Легкий моросящий дождь', 'Overcast': 'Пасмурно', 'Heavy rain': 'Сильный дождь',
    'Patchy light drizzle': 'Возможен мелкий моросящий дождь', 'Sunny': 'Солнечно', 'Clear': 'Ясно',
    'Moderate or heavy rain shower': 'Умеренный или сильный ливень', 'Cloudy': 'Облачно', 'Mist': 'Туман',
    'Moderate rain at times': 'Временами умеренный дождь', 'Thundery outbreaks possible': 'Возможны грозовые вспышки'
    }

TRANSLATION_WIND = {
    'N': 'Север', 'NNE': 'Северо-северо-восток', 'NE': 'Северо-восток', 'ENE': 'Восток-северо-восток',
    'E': 'Восток', 'ESE': 'Восток-юго-восток', 'SE': 'Юго-восток',  'SSE': 'Юго-юго-восток',
    'S': 'Юг', 'SSW': 'Юго-юго-запад', 'SW': 'Юго-запад', 'WSW': 'Запад-юго-запад', 'W': 'Запад',
    'WNW': 'Запад-северо-запад', 'NW': 'Северо-запад', 'NNW': 'Северо-северо-запад'
    }


def revers_str_data(string):
    string_year, string_month, string_day, string_time = string[0:4], string[5:7], string[8:10], string[11:16]
    new_string = string_day + '-' + string_month + '-' + string_year + ' ' + string_time
    return new_string


def get_weather(place):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=a72f7c3e2a14440994b105947232606&q={place}&days=1&aqi=no&alerts=no'
    params = {'text': place}
    res = requests.get(url, params=params)
    data = res.json()
    temp_C = str(round(data['current']['temp_c'])) + ' °C'
    wind_metr_sek = str(round(int(data['current']['wind_kph']) * 0.277777778, 2)) + ' м/сек'

    if TRANSLATION_WEATHER.get(data['current']['condition']['text']) is not None:
        condition = TRANSLATION_WEATHER.get(data['current']['condition']['text'])
    else:
        condition = data['current']['condition']['text']

    is_day = 'День' if data['current']['is_day'] == 1 else 'Ночь'
    print(f"\nСейчас в городе {place} (Страна: {data['location']['country']}) {is_day}\n"
          f"Локальное время: {revers_str_data(data['location']['localtime'])}\n"
          f"Состояние погоды: {condition}\nОблачность: {data['current']['cloud']} %\n"
          f"Температура: {temp_C}\nСкорость ветра: {wind_metr_sek}\n"
          f"Направление ветра: {TRANSLATION_WIND.get(data['current']['wind_dir'])}\n"
          f"(Последнее обновление данных было: {revers_str_data(data['current']['last_updated'])})")


while True:
    user_answer = input('\n1) Узнать погоду\n'
                        '2) Выйти\n– ')
    if user_answer == '2':
        print('Программа завершила свою работу')
        break
    elif user_answer == '1':
        user_answer2 = input('Введите место: ')
        try:
            get_weather(user_answer2)
        except[KeyError]:
            print('Ошибка, введите корректные данные')
    else:
        print('Ошибка, введите корректный вопрос')




