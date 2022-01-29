"""
Урок 2. Некоторые встроенные типы и операции с ними
"""
# что такое типы и как их проверять
a = 1
print(type(a))

print(isinstance(a, int))
print(isinstance(a, bool))
if not isinstance(a, str):
    print('объект должен быть объектом типа string')

print(type(a) == float)

# Как смотреть методы объекта
im_list = list()  # []
print(dir(im_list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# Методы списка
im_list.append(100)
print(f"{im_list} - {len(im_list)}")

im_list.extend([10, 15])
print(f"{im_list} - {len(im_list)}")

im_list.append([10, 15])
print(f"{im_list} - {len(im_list)}")

im_list.extend([10, 15])
print(f"{im_list} - {len(im_list)}")

search_value = 10
print('Количество искомого', 10, '-', im_list.count(search_value))

year = ['январь', 'февраль', 'март', 'апрель', 'май']
print(year)

element_1 = year.pop()
print(element_1)
print(year)

element_1 = year.pop(2)
print(element_1)
print(year)

print(year.index('январь'))
# print(year.index('декабрь'))

# .insert() и .remove()
year.insert(2, 'ноябрь')
print(year)

year.append('ноябрь')
print(year)

while year.count('ноябрь'):
    print('Я сейчас удалю ноябрь')
    year.remove('ноябрь')
print(year)

# Реверсы и срезы списков
print('Реверс списка in_place')
print(id(year), year)
year.reverse()
print(id(year), year)

print('Реверс списка not in_place')
print(id(year), year)
year_reversed = list(reversed(year))
print(id(year_reversed), year_reversed)

# print(list(range(1, 100, 2)))
new_list = list(range(1, 100, 2))
print(id(new_list), new_list)
new_list_2 = new_list[::-1]
print(id(new_list_2), new_list_2)

# параметры среза obj[start=0, stop=len(obj), step=1]
print('Hello world!'[6:-1:])
print('Hello world!'[::-1])

"""
ord('а')
1072
ord('б')
1073
ord('в')
1074
ord('я')
1103
ord('Я')
1071
ord('Я') - ord('я')
-32
chr(1103)
'я'
chr(1103-32)
'Я'
chr(1072-32)
'А'
"""
year.reverse()
year.append('декабрь')
# Сортировки списков
print('Сортировка in_place')
print(id(year), year)
year.sort()
# year.sort(reverse=True)
print(id(year), year)

print('Сортировка not in_place')
print(id(year), year)
# year_sorted = sorted(year)
year_sorted = sorted(year, reverse=True)
print(id(year_sorted), year_sorted)

# Кортежи
import sys

some_list = ['hello', True, 'word', 1, 2.2]
print(type(some_list), sys.getsizeof(some_list), some_list)
some_tuple = ('hello', True, 'word', 1, 2.2)
print(type(some_tuple), sys.getsizeof(some_tuple), some_tuple)


def search_methods_obj(obj):
    """Находит методы объекта Python"""
    for element in dir(obj):
        if not element[:2:] == '__':
            print(element, end=' ')
    print()


print('Методы списка:')
search_methods_obj(some_list)

print('Методы кортежа:')
search_methods_obj(some_tuple)


# Нюансы присваивания и копирования объектов
a = [['hello'], 10]
b = a
print(id(a), id(b))
b[1] = 15
print(a, b)
print(id(a), id(b))

from copy import copy, deepcopy

a = [['Привет'], 10]
b = copy(a)
print(id(a), id(b))
b[1] = 15
print(a, b)
b[0][0] = 'world'
print(id(a), id(b))
print(a, b)

print('\n\n')
a = [['Привет'], 10]
b = deepcopy(a)
print(id(a), id(b))
b[1] = 15
print(a, b)
b[0][0] = 'world'
print(id(a), id(b))
print(a, b)


# Работа со строками
hello = list('Hello world!')
print(hello)


print('Форматирование строк')
name = 'Артём'
minute = 5
print('Проснись, ' + name + '! Вебинар скоро закончится. Осталось ' + str(minute) + ' минут.')
print('Проснись, %s! Вебинар скоро закончится. Осталось %d минут.' % (name, minute))
print('Проснись, {:^20}! Вебинар скоро закончится. Осталось {:.2f} минут.'.format(name, minute))
print(f'Проснись, {name}! Вебинар скоро закончится. Осталось {minute} минут.')

# split(), параллельное присваивание с распаковкой
# join()
# upper() и lower()
# title() и capitalize()

print(year)
print(', '.join(year))

# реверс строки
message = 'екшамод к ьрепет илангоп'
print(message[::-1])

print('end')

