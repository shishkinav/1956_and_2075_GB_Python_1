""""
Проценты и прочеее....
"""
def transform_string(number:int) ->str:
    if number%10==0:
        return str(number)+" процентов"
    elif number%10 ==1:
        return str(number) + " процент"
    elif number%10 <=4:
        return str(number) + " процента"
    elif number%10 <=9:
        return str(number) + " процентов"

for n in range(1, 101):# по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
print("The third part of the homework of lesson 1 is successfully done 27.01.2022")