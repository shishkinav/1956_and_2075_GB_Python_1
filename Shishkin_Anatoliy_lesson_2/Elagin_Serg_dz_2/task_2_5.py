from random import uniform
import copy

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    # приведение к типу "строка"
    i = 0
    for element in list_in:
        price = str(element)
        list_in.insert(i, price.split('.'))
        del list_in[i + 1]
        i += 1
    # формат строки
    i = 0
    for element in list_in:
        if len(element[1]) < 2:
            element[1] = '0' + element[1]
        price = ' руб '.join(element)
        list_in.insert(i, price + ' коп, ')
        del list_in[i +1]
        i += 1
    str_out = ''.join(list_in)        #"здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    my_list.sort()
    return my_list, "отсортированный результирующий список"


# зафиксируйте здесь информацию по исходному списку my_list
print(id(my_list))
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(id(result_2))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    my_list_rev = copy.copy(my_list)
    list_out = list(reversed(my_list_rev)), "список элементов в списке по убыванию"
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = ["список из пяти самых больших элементов"]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)





