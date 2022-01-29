def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_list = 0
    for i in dataset:
        sum_digits = 0
        elemen_of_my_list = i
        while i !=0:
            digit = i % 10
            sum_digits += digit
            i = i // 10
        if sum_digits % 7 == 0:
            sum_list += elemen_of_my_list
    return sum_list # Верните значение полученной суммы

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    sum_list = 0
    for i in dataset:
        i += 17
        sum_digits = 0
        elemen_of_my_list = i
        while i != 0:
            digit = i % 10
            sum_digits += digit
            i = i // 10
        if sum_digits % 7 == 0:
            sum_list += elemen_of_my_list
    return sum_list  # Верните значение полученной суммы


my_list = []
for i in range(1, 1001, 2):
    my_list.append(i**3)   # Соберите нужный список по заданию >>>> Создать список, состоящий из кубов нечётных чисел `от 1 до 1000`


result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
