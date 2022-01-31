from random import uniform
import copy

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    str_out =''
    for element in list_in:
        int_part = element
        float_part = element
        int_part = int_part // 1
        float_part = (float_part - int_part + 0.001) * 100
        int_part = f'{int(int_part)} руб '
        if int(float_part) < 10:
            float_part = f'0{int(float_part)} коп, '
        else:
            float_part =  f'{int(float_part)} коп, '
        str_out += int_part + float_part     #"здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    my_list.sort()
    return my_list



# зафиксируйте здесь информацию по исходному списку my_list
print('id  my_list:',id(my_list) )    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#                                                                                        |
result_2 = sort_prices(my_list)       #                                                 |
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом     | id my_list = id result_2
#                                                                                       | соответственно это один и тот же обьект
#                                                                                        |
print('id result_2:',id(result_2) )    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(result_2,"отсортированный результирующий список")


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    my_list_rev = copy.copy(my_list)
    list_out = list(reversed(my_list_rev))
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3, "список элементов в списке по убыванию")


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = []
    _ = [my_list[0]]
    for elem in my_list:                  # выберает 5 наибольших значений
        if _[0] < elem:
            _.insert(0,elem)
    del _[5:len(_)]
    # если нельзя использовать sort() то реверс "в ручную"
    n = len(_)-1
    while n != -1:
        _.append(_[n])
        n -= 1
    del _[0:int(len(_)/2)]
    list_out = _
    return  list_out


result_4 = check_five_max_elements(my_list)
print(result_4, "список из пяти самых больших элементов")




#end