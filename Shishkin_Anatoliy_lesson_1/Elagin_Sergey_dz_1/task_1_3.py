def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if (n + 9) % 10 == 0 and n != 11:
        transformed_string = f'{n} процент'
    else:
        if n > 11 and n <= 14:
            transformed_string = f'{n} процентов'
        else:
            if (n % 10) >= 2 and (n % 10) <= 4:
                transformed_string = f'{n} процента'
            else:
                transformed_string = f'{n} процентов'
    return transformed_string #'верните отформатированную строку'
for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))










