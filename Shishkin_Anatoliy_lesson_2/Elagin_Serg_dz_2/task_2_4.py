def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    # extracting
    i = 0
    for element in list_in:
        cut_name = element.split(' ')
        list_in[i] = ([cut_name[-1]])
        i += 1
    # converting
    i = 0
    for element in list_in:
        convert_name = ''.join(element)
        list_in.insert(i, 'Привет,  ' + convert_name.capitalize() + '!')
        del list_in[i + 1]
        i += 1
    list_out = list_in       #["здесь должены оказаться результирующие строковые приветствия"]
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)





#end






