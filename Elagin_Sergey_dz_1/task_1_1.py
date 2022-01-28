def convert_time(duration):
    view = ''
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minuts = (duration - hours * 3600 - days * 86400) // 60
    sec = duration - minuts * 60 - hours * 3600 - days * 86400
    if days != 0:
        view = f'{days} days, {hours} hours, {minuts} minutes, {sec} seconds'
    elif hours != 0:
        view = f'{hours} hours, {minuts} minutes, {sec} seconds'
    elif minuts !=0:
        view = f'{minuts} minutes, {sec} seconds'
    else:
        view = f'{sec} seconds'
    return view


duration = 400153
result = convert_time(duration)
print(result)

# несколько значений
print('*'*100)
duration_list = [10, 100, 1000, 10000]
for i in duration_list:
    result = convert_time(i)
    print(result)