"""
Урок 4. Работа с модулями и пакетами
"""
# Батарейки для Python: pypi.org
# https://pypi.org/project/num2words/
# from num2words import num2words


# print(num2words(42))                                # forty-two
# print(num2words(42, to='ordinal'))                  # forty-second
# print(num2words(42, to='ordinal_num'))              # 42nd
# print(num2words(42, to='year'))                     # forty-two
# print(num2words(12.42, to='currency'))              # twelve euro, forty-two cents
# print()
# print(num2words(42, lang='ru'))                     # сорок два
# print(num2words(42, to='ordinal', lang='ru'))       # сорок второй
# print(num2words(42, to='ordinal_num', lang='ru'))   # 42
# print(num2words(42, to='year', lang='ru'))          # сорок два
# print(num2words(12.42, to='currency', lang='ru'))   # двенадцать евро, сорок два цента


# Модули и пакеты в Python
# hello_module.py
import hello_module


hello_module.say_hello('Виталий')


# External Libraries в PyCharm
# requests
import requests.utils

# Ctrl + Alt + O — PyCharm автоматически поправит импорты в скрипте и уберёт лишнее

# response = requests.get('https://gb.ru')
# encodings = requests.utils.get_encoding_from_headers(response.headers)
# print(encodings)

import os
import json

import requests

from hello_module import say_hello

# Внимание: сначала должны быть импорты из стандартной библиотеки, потом модули
# и пакеты третьих лиц, и только потом — ваши.


# создаём свой CLI - my_cli.py
# Модуль sys: запуск скрипта с параметрами
# Напишем скрипт для сложения чисел в командной строке (терминале)

# Рекомендуем в будущем изучить модуль argparse — он позволяет писать серьёзные инструменты для командной строки.
# argparse - https://docs.python.org/3.8/library/argparse.html#module-argparse


# Модуль time: профилируем время выполнения участков кода
# time_profiler.py

# Модуль datetime: работа с датой и временем
# datetime_difference.py

# Подсказка ко второму ДЗ
# cbr_parser
# python cbr_parser/utils.py
# https://pypi.org/project/pyquery/


print('end')
