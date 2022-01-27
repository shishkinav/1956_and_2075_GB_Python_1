# Реализация вывода информации о продолжительности промежутка времени в секундах
"""
Непонятно сколько вариантов можно наплодить и сколько видов намутить .... со списком или без так или сяк
Надо делать ввод через консоль или зафигачить в цикле огромное количество этих дурейшенов....
"""

def convert_time(duration:int)-> str:
    if duration<60:
       res_date=(duration, 'сек')
    elif duration <3600:
        res_date=(duration//60, 'мин', duration%60, 'сек')
    elif duration <86400:
        res_date=(duration//3600, 'час', duration%3600//60, 'мин', duration%3600%60, 'сек')
    elif duration<31536000:
        res_date = (duration//86400, 'дн', duration%86400//3600, 'час', duration%86400%3600//60, 'мин', duration%86400%3600%60, 'сек')
    elif duration >31536000:
        res_date=('слишком большой промежуток больше 1 года')
    res_date = str (res_date)
    res_date= res_date.replace(',','')
    res_date = res_date.replace ( "'",'' )
    res_date = res_date.replace ( "(", '' )
    res_date = res_date.replace ( ")", '' )
    return str(res_date)
    #print('The first part of the homework of lesson 1 is successfully done ')

def convert_time2(duration:int)-> str: # через список - так код меньше
    if duration<60:
       my_list=[duration, 'сек']
    elif duration <3600:
       my_list=[duration//60, 'мин', duration%60, 'сек']
    elif duration <86400:
        my_list =[duration//3600, 'час', duration%3600//60, 'мин', duration%3600%60, 'сек']
    elif duration<31536000:
        my_list = [duration//86400, 'дн', duration%86400//3600, 'час', duration%86400%3600//60, 'мин', duration%86400%3600%60, 'сек']
    return my_list

print('Фиксированный ввод 1!')
duration=53
print(duration)
print (convert_time(duration))
duration=153
print(duration)
result=convert_time(duration)
print(result)
duration=4153
print(duration)
result=convert_time(duration)
print(result)
duration=400153
print(duration)
result=convert_time(duration)
print(result,'\n')

print('Фиксированный ввод 2!')
duration=53
print(duration)
print(*convert_time2(duration), sep=' ')
duration=153
print(duration)
print(*convert_time2(duration), sep=' ')
duration=4153
print(duration)
print(*convert_time2(duration), sep=' ')
duration=400153
print(*convert_time2(duration), sep=' ')
print ('\n')

print('<<<<Ручной ввод с квлавиатуры 1>>>>')
try: # Проверка на ошибку, забегая вперед (привычка из VB), google в помощь
    duration_manual=input(f"Введите промежуток времени в секундах (целым числом):" '\n')
    result=convert_time(int(duration_manual))# преобразуем в целое число
    print ( result )
except ValueError:
    print(type(duration_manual))
    print("Ошибка ввода! (ввод только цифрами), перезапустите расчет")
else: pass
print('<<<<Ручной ввод с квлавиатуры 2>>>>')
while True:
    try:  # Проверка на ошибку, забегая вперед (привычка из VB), google в помощь
        duration_manual = input ( f"Введите промежуток времени в секундах (целым числом):" '\n' )
        result = convert_time ( int ( duration_manual ) )  # преобразуем в целое число
        print ( result )
    except ValueError:
        print ( type ( duration_manual ) )
        print ( "Ошибка ввода! (вводите только цифры)" )
    else:
        print ( 'The first part of the homework of lesson 1 is successfully done 27.01.2022' )
        break
