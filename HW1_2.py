def sum_list_1(dataset: list) -> int:
    sum_del_7 = 0
    for i in range(len(dataset)):
        sum = 0
        num = dataset[i]
        while (num != 0):
            sum = sum + num % 10
            num = num // 10
        if sum % 7 == 0:
            sum_del_7 = + dataset[i]
    return sum_del_7


def sum_list_2(dataset: list) -> int:
    sum_del_7_2 = 0
    for i in range(len(dataset)):
        dataset[i] = dataset[i] + 17  # Прибавил число 17 к каждому элементу
    # print ('к кубам прибавляем 17')
    # print(dataset)
    for i in range(len(dataset)):
        sum = 0
        num = dataset[i]
        while (num != 0):  # До тех пока не станет ноль
            sum = sum + num % 10  # берем первую цифру
            num = num // 10  # сдвигаемся на следующую цифру
        if sum % 7 == 0:
            sum_del_7_2 = +dataset[i]
    return sum_del_7_2
my_list = []  # объявляем пустой лист
for cub_X in range(1, 1000, 2):
    my_list.append(cub_X ** 3)
# print("Кубы нечетных чисел от 1 до 1000")
# print(my_list) # Отображается список кубов нечетных чисел от 1 до 1000

result_1 = sum_list_1(my_list)
result_2 = sum_list_2(my_list)

print(' Общая сумма чисел, сумма чисел которых делится нацело на 7')
print(result_1)  # По моему избыточная переменная
print(' Общая сумма чисел, сумма чисел которых делится нацело на 7, после прибавки 17 к кубам')
print(result_2, '\n')
print('The second part of the homework of lesson 1 is successfully done 27.01.2022')

