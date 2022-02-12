"""
Урок 6. Работа с файлами
"""
# файлик hello.txt

file_1 = open('hello.txt', encoding='utf-8')
# print(dir(file_1))
"""
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 
'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 
'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines'
"""
content = file_1.read()
print(content)
file_1.close()
# print(content)
# print(file_1.read())  # ValueError: I/O operation on closed file.

file_2 = open('hello.txt', encoding='utf-8')
print(file_2.readline())
print(file_2.readline())
print(file_2.readline())
print(
    isinstance(file_2.readline(), str)
)
print(file_2.readline() == '')
file_2.close()

print('\n\n Считывание файла через for построчно')

file_3 = open('hello.txt', encoding='utf-8')
for line in file_3:
    print(line.strip(), end='')
file_3.close()

print('\n\n Считывание файла через readlines')

file_4 = open('hello.txt', encoding='utf-8')
print(file_4.readlines())
file_4.close()


print('\n\n')

# менеджер контекста
# with open('qwerty.txt', 'w+', encoding='utf-8') as fw:
#     print('Какую-то строку', file=fw)
#     fw.write('asdf\nfdfg\nasdf\n')
#     fw.seek(0)
#     print(fw.read())

# with open('qwerty_2.txt', 'a+', encoding='utf-8') as my_qwerty_file:
#     from datetime import datetime
#
#     current_time = datetime.now()
#     # my_qwerty_file.write(current_time)
#     my_qwerty_file.write(f'{current_time}\n')


# summator
import random


tasks = [f'{random.randrange(1, 10)} {random.randrange(1, 10)}\n' for _ in range(10)]

# формируем тестовые данные для разбора
# with open('trash/tasks_summator.txt', 'w', encoding='utf-8') as fw:
#     # fw.write(str(tasks))
#     fw.writelines(tasks)


def send_sum(value_1: int, value_2: int):
    """Простейшая функция суммирования двух значений"""
    return value_1 + value_2


result_1 = 0
with open('trash/tasks_summator.txt') as fr:
    for row in fr.readlines():
        v1, v2 = row.split(' ')
        result_1 += send_sum(*map(int, [v1, v2]))

print('1 - Результат рассчитанной суммы:', result_1)


print('\n\n')

result_2 = 0
with open('trash/tasks_summator.txt', 'r') as fr:
    for row in fr:
        v1, v2 = row.split(' ')
        result_2 += send_sum(*map(int, [v1, v2]))

print('2 - Результат рассчитанной суммы:', result_2)

print('\n\n')

result_3 = 0
with open('trash/tasks_summator.txt', 'r') as fr:
    while True:
        row = fr.readline()
        if not row:
            break
        v1, v2 = row.split(' ')
        result_3 += send_sum(*map(int, [v1, v2]))

print('3 - Результат рассчитанной суммы:', result_3)


# json
import json

my_dataset = [
    {'name': 'Стас', 'level': 15},
    {'name': 'Софья', 'level': 33}
]

# with open('trash/tasks_json.json', 'w', encoding='utf-8') as fw:
#     # json_str = json.dumps(my_dataset, ensure_ascii=False, indent=2)
#     # fw.write(json_str)
#     json.dump(my_dataset, fw, ensure_ascii=False, indent=2)

# with open('trash/tasks_json.json', 'r', encoding='utf-8') as fr:
#     # json_str = fr.read()
#     # dataset = json.loads(json_str)
#     dataset = json.load(fr)
#     print(type(dataset), dataset)


# pickle
import pickle


data = {
    1: [random.randrange(1, 10) for _ in range(5)],
    2: ('Я какая-то строка', b'binary data'),
    3: {None, True, False}
}


# with open('trash/data.pickle', 'wb') as fw:
#     pickle.dump(data, fw)
#     # data_bytes = pickle.dumps(data)
#
# with open('trash/data.pickle', 'rb') as fr:
#     data_new = pickle.load(fr, encoding='utf-8')
#     # dataset = pickle.loads(data_bytes)
#
# print(type(data_new), data_new)
# print(type(data_bytes), data_bytes)
# print(type(dataset), dataset)


# Профилируем создания файла в байтах и текстового, проверяем размер
from time import perf_counter

# nums = [random.random() * 10 ** 6 for _ in range(10 ** 6)]

# start = perf_counter()
# with open('trash/random_million.json', 'w', encoding='utf-8') as f:
#     json.dump(nums, f)
# print(f'json saved: {perf_counter() - start}')
#
# start = perf_counter()
# with open('trash/random_million.pickle', 'wb') as f:
#     pickle.dump(nums, f)
# print(f'pickle saved: {perf_counter() - start}')
#
#
# # профилируем считываение файла в байтах и текстового
# start = perf_counter()
# with open('trash/random_million.json', 'r', encoding='utf-8') as f:
#     nums = json.load(f)
# print(f'json loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}')
#
# start = perf_counter()
# with open('trash/random_million.pickle', 'rb') as f:
#     nums = pickle.load(f)
# print(f'pickle loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}')


# Чтение файлов порциями
# chunk_size = 256
# with open('trash/random_million.json', 'r') as f:
#     str_data = []
#     while True:
#         chunk = f.read(chunk_size)
#         if not chunk:
#             break
#         str_data.append(chunk)
#     nums = json.loads(''.join(str_data))
# print(f'{type(nums)}, {len(nums)}')
#
# with open('trash/random_million.pickle', 'rb') as f:
#     binary_data = bytearray()
#     while True:
#         chunk = f.read(chunk_size)
#         if not chunk:
#             break
#         binary_data.extend(chunk)
#     nums = pickle.loads(binary_data)
# print(f'{type(nums)}, {len(nums)}')


# encode и decode
hello_text = 'Привет мир'
txt_binary = hello_text.encode(encoding='utf-8')
print(type(txt_binary), txt_binary)
txt_origin = txt_binary.decode(encoding='utf-8')
print(type(txt_origin), txt_origin)


print('the end')

