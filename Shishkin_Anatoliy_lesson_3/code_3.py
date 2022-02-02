"""
Урок 3. Функции. Словари
"""
def func(a: int, b: int) -> int:
    """Пример простейшей функции"""
    c = a + b
    return c


a = 3
b = 5
value = func(a, b)
print(value)
print()

value = func(5, 5)
print(value)

callback = func  # алиас callback для объекта func
print(type(callback), callback(5, 5))

text_example_1 = 'Опыт выполнения домашних заданий предыдущих уроков наверняка подсказывает вам, ' \
                 'что нужен какой-то способ для повторного использования уже написанного кода.'
text_example_2 = 'Один из способов был изобретен очень давно — обособление фрагментов кода в функции. ' \
                 'Мы уже говорили о них.'
from utils.string_transform import clear_punctuation, lower_and_split


# new_text = clear_punctuation(text_example_1)
# print(lower_and_split(new_text))
#
# new_text_2 = clear_punctuation(text_example_2)
# print(lower_and_split(new_text_2))

for own_text in (text_example_1, text_example_2):
    new_text = clear_punctuation(own_text)
    print(lower_and_split(new_text))


# Возвращаем callback
# упрощённый пример
nums = ['1578.4', '892.4', '354.1', '871.5']
value = 0
for num in nums:
    value += float(num)
print(f'value = {value}')

# решение усложнённое
print(
    sum(
        map(float, nums)
    )
)

# docstring - используем help() для получения имеющейся документации
# help(str.upper)
# help(clear_punctuation)
# help(list)


# Области видимости переменных
# def say_hello_wrapper():
#     name = 'Петр'
#
#     def say_hello():
#         print(name)
#
#     say_hello()
#
#
# name = 'Иван'
# say_hello_wrapper()
#
# print('\n\n')
#
# # запрещённый проброс переменной из локальной области в глобальную
# def say_hello():
#     global name
#     name = 'Петр'
#     print(name)
#
#
# name = 'Иван'
# print(name)  # Иван
# say_hello()  # Петр
# print(name)


# пример использования nonlocal
# def counter():
#     num = 0
#
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#
#     return incrementer
#
#
# v = counter()
# print(v())
# print(v())
# print(v())


print()
# Словари Python (Ассоциативные массивы)
pers_1 = ['pikachu', 87.9, 103]
pers_2 = ['smurfik', 10.0, 66]


# def get_info(data):
#     print(f'Никнейм - {data[0]}, health - {data[1]}, level - {data[2]}')
#
#
# get_info(pers_1)
# get_info(pers_2)
print()


# upgrade pers
pers_1_adv = {
    "nickname": 'pikachu',
    "health": 87.9,
    "level": 103
}
pers_2_adv = {
    "nickname": 'smurfik',
    "health": 10.0,
    "level": 66
}


def get_info(dataset: dict) -> str:
    print(f'Никнейм - {dataset["nickname"]}, health - {dataset["health"]}, level - {dataset["level"]}')


get_info(pers_1_adv)
get_info(pers_2_adv)
print()

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""

# Словари: .get() и .setdefault()
print(pers_1_adv.get('sex'))
print(pers_1_adv.get('sex', 'средний'))
print(pers_1_adv.get('nickname', 'верхний'))
print(pers_1_adv)
print()

print(pers_1_adv.setdefault('sex', 'man'))
print(pers_1_adv)
print(pers_1_adv.setdefault('nickname', 'Андрей'))
print(pers_1_adv)
print()

# Словари: .update() и .popitem()
print(pers_1_adv.popitem())
print(pers_1_adv)
print(pers_1_adv.pop('level'))
print(pers_1_adv)
print()


dataset = {
    'mail.ru': '94.100.180.201',
    'geekbrains.ru': '178.248.232.209',
    'amazon.com': '205.251.242.103'
}

for key in dataset:
    print(key)

print()

for key in dataset.keys():
    print(key)

print(type(dataset.keys()))

for key, value in dataset.items():
    print('{}={}'.format(key, value))

print(dataset.values())  # возвращает значения словаря

print('\n\n')
# Позиционные аргументы и *args
from utils.tools import own_sum, own_sum_upgrade


print(f'own_sum([1, 5, 89]) = {own_sum([1, 5, 89])}')
# print(own_sum(1, 5, 89))
print(f'own_sum_upgrade(1, 5, 89) = {own_sum_upgrade(1, 5, 89, 100, 100)}') # НЕТ ОШИБКИ - WHY?
print(own_sum([1, 5, 89]) == own_sum_upgrade(1, 5, 89))

# разбираем распаковку
a = 5
b = 10
a, b = (b, a)

own_list = ['Дмитрий', 1, 2, 3, 4, 5]

# name, health, level = own_list
# print(name, health, level)
name, health, *others = own_list
print(name, health, type(others), others)
own_list_2 = list((name, health, *others))
print(own_list_2)


# Модуль random
from random import randrange, randint, choice


numbers = list()
for n in range(1, 11):
    numbers.append(n * 11)

print(numbers)
print()
idx = randrange(len(numbers))  # как пользоваться randrange
print(f'idx = {idx}')
print(f'numbers[{idx}] = {numbers[idx]}')
print()
new_idx = randint(0, len(numbers) - 1)  # как пользоваться randint
print(f'new_idx = {new_idx}')
print(f'numbers[{new_idx}] = {numbers[new_idx]}')
print()
print(f'Случайное значение из списка {numbers} получили {choice(numbers)}')
print()
# choices, sample и shuffle - разбираем самостоятельно в методичке есть ссылки


# Необязательные аргументы, именованные аргументы - **kwargs

def my_game(count_game: int, luck: float = 0.00, **kwargs) -> None:
    """Играем на стандартном кубике"""
    if luck > 100:
        luck = 100.00
    # end_number = 6
    end_number = kwargs.get('count_edge', 6)
    start_number = 1 + int(((end_number - 1) * luck) / 100)
    for _ in range(count_game):
        print(f'При броске на кубике выпало: {randint(start_number, end_number)}')


my_game(2)
my_game(2, 100.00)
my_game(2, luck=100, count_edge=12)
my_game(2, luck=100, count_edge=12, hot='sale', kot='geh')
print()


# filter(), map(), zip() и lambda-функции
new_numbers = [value * 11 for value in range(20)]
print(f'new_numbers = {new_numbers}')
print()

own_filter_result = filter(lambda obj: obj % 10 == 5, new_numbers)
# print(list(own_filter_result))
print(*own_filter_result)

def my_filter(obj):
    return obj % 10 == 5

own_filter_result_2 = filter(my_filter, new_numbers)
print(*own_filter_result_2)


map_result = map(lambda obj: obj // 10, new_numbers)
ll = list(map_result)
print('map_result =', ll, f'длина - {len(ll)}')
print()


user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
user_logins = ['ivan', 'petr', 'olga', 'sergey']
user_roles = ['user', 'staff', 'admin']

zip_result = zip(user_names, user_logins, user_roles)
print('zip_result =', tuple(zip_result))
print()


print('end')

