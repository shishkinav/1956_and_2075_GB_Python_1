"""
Урок 1. Знакомство с Python
"""

# однострочный

print('Hello world!')

# Арифметические операции
# Ctrl 2 раза, второй раз держим кнопку + стрелки
print(37 + 7)
print(37 - 7)
print(37 * 7)
print(37 / 7)
print(37 // 7)
print(37 % 7)
print(37 ** 7)

# Логические операции
# ctrl + D
print(5 > 6)
print(5 < 6)
print(5 == 6)
print(5 != 6)
print(5 >= 6)
print(5 <= 6)

# and, or
print(True and True)
print(False and True)
print(False and False)

print(True or True)
print(False or True)
print(False or False)

"""
>>> not True
False
>>> not False
True
"""
print('\n')

my_var = 1
print(my_var + 6)

my_list = ['молоко', "кефир"]
print(my_list)
print(type(my_list))
print(type(my_list), my_list)
my_var = 'Я какая-то переменная с "кавычками"'
print(my_var)

# name = input('Введите имя:\n')
# print(f'Вас зовут: {name}')


# int
my_int = 50
print(type(my_int))

# str
my_str = 'qwe'
print(type(my_str))

# float
my_float = 95.654
print(type(my_float))

# bool
my_bool = True  # False
print(type(my_bool))


a = 0
b = 5
c = -9

out = b > a and c < 0
out_2 = not((b > a or c < 0) and b == 5)
print(out, out_2)

room = 13
do_clean: bool = room // 10 > 7 or room % 10 == 3
print(type(do_clean), do_clean)

if '<логическое выражение 1>':
    pass  # блок кода для логического True первого выражения
elif '<логическое выражение 2>':
    pass  # блок кода для логического True второго выражения
else:
    pass  # блок кода для логического False


user_pass = 'qwerty'
admin_pass = 'admin'
# if user_pass == input('Введите пароль:\n'):
#     print('Авторизован успешно')
#     if admin_pass == input('Введите пароль админа:\n'):
#         print('rooted')
#     else:
#         print('not rooted')
# else:
#     print('Пароль не верный')

color = 'red'
if color == 'green':
    print('зеленый')
elif color == 'red':
    print('красный')
elif color == 'blue':
    print('синий')
else:
    print('цвет неизвестен')

my_list = [100, 'qwe', 540.1, True]
print(my_list[1])
my_list.append(['молоко', 'кефир'])
print(my_list)


# циклы while, for in

nums = [10, 20, 30, 40]
indx = 0

"""
while '<логическое выражение>':
    pass  # тело цикла
"""
# while indx < len(nums):
#     print(nums[indx] + 1)
#     indx = indx + 1  # indx += 1, indx -= 1
#
# while True:
#     print('я очередная итерация цикла')
#     break

# for element in nums:
#     print(f'На этом шаге я владею значением {element}')

# for idx, el in enumerate(nums, start=1):
#     print(f'На шаге {idx} я владею значением {el}')

# range(start=0, stop, step=1)
for i in range(3, 11, 2):
    print(i)

for i in range(10, 3, -2):
    print(i)

# Общее представление о функции для выполнения практических заданий
def my_first_func(obj):
    my_result = f'В функцию поступил объект: {obj}'
    return my_result


my_var = [1, 2, 3]
print(my_first_func(my_var))
print(type(my_first_func(my_var)))
print(type(my_first_func))

print('end')

