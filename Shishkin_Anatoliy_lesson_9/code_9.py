"""
Урок 9. Объектно-ориентированное программирование. Введение
"""
# определение класса
from datetime import datetime


class Woman:
    # глобальные атрибуты класса
    name: str = 'Алина'
    birthday: datetime = datetime(year=1998, month=2, day=24)

    # методы класса
    def introduce_youself(self):
        print(f"I'm {self.__class__.__name__}")

    def get_info(self):
        print(f'Давай знакомиться: я - {self.name} и я родилась {self.birthday.strftime("%d %B %Y")}')

    def say(self, message: str):
        print(f'{self.name} сказала нам: "{message}"')


girl = Woman()
print(type(girl), girl)
girl.introduce_youself()
girl.get_info()
girl.say('С днём рождения меня!')
# girl_2 = Woman()
# girl_2.name = 'Ксения'
# print(girl.name, girl_2.name, Woman.name)
# Woman.name = 'Елена'
# print(girl.name, girl_2.name, Woman.name)
# print('\n')


class Warehouse:
    count: int = 0

    def new_build(self, storage_capacity: float, region: str):
        """Объявляет о постройке нового склада"""
        self.storage_capacity = storage_capacity
        self.region = region
        Warehouse.count += 1  # инкрементируем общее количество складов


# warehouse_1 = Warehouse()
# warehouse_1.new_build(555.55, 'Москва')
# print(warehouse_1.storage_capacity, warehouse_1.region, f'Всего складов: {warehouse_1.count}')
# warehouse_2 = Warehouse()
# warehouse_2.new_build(150, 'Волгоград')
# print(warehouse_2.storage_capacity, warehouse_2.region, f'Всего складов: {warehouse_2.count}')
# print('\n')


# Конструктор __init__
class Rabbit:
    auto_count: int = 0

    def __init__(self):
        self.local_attr = True
        Rabbit.auto_count += 1
        local_var = 'я локальная переменная'


rabbits = [Rabbit() for _ in range(10)]
first_rabbit = rabbits[0]
print(f'Наполдили кроликов - {Rabbit.auto_count} шт.')
print('\n', first_rabbit.local_attr)


"""
Модификаторы доступа

Public (публичный);
Protected (защищённый);
Private (приватный).
"""
class Dog:
    def __init__(self):
        self.voice = 'гав-гав'
        self._color_hair = 'серый'
        self.__place = 'будка во дворе'


dog = Dog()
print(dog.voice)
print(dog._color_hair)
# print(dog.__place)
print('\n')


# Инкапсуляция
class Ant:
    __species: str = 'коричневый'

    def __get_species(self):
        print('Приватный метод')


ant = Ant()
ant._Ant__get_species()
print(ant._Ant__species)
print('\n')


# Наследование
import time


class People:
    """Так зарождалось всё человечество)))"""
    def __init__(self, name: str, birthday: datetime):
        self.name = name
        self.birthday = birthday

    def introduce_yourself(self):
        return f"I'm {self.__class__.__name__}", self.__get_info()

    def __get_info(self):
        return dict(name=self.name, birthday=self.birthday.strftime("%d %B %Y"))


class Man(People):
    sex: str = 'm'

    def working(self, sleeping: int = 5):
        """Мужик должен уметь работать"""
        while sleeping:
            print(f'Осталось спать секунд: {sleeping}')
            time.sleep(1)
            sleeping -= 1
        print('Поработали, теперь можно и домой!')


worker = Man('Гаррик', datetime(year=1993, month=10, day=28))
message, info = worker.introduce_yourself()
print(f' {3 * "-||-"} '.join(
    map(str, [message, info, type(message), type(info)])
))
# worker.working()
print('\n')


class Woman2(People):
    sex: str = 'w'

    def __init__(self, name: str, birthday: datetime, secret: str):
        super().__init__(name, birthday)
        # self.name = name
        # self.birthday = birthday
        self.secret = secret


girl_2 = Woman2('Алина', datetime(year=1998, month=2, day=24), 'Я люблю рисовать!')
message, info = girl_2.introduce_yourself()
print(f' {3 * "-||-"} '.join(
    map(str, [message, info, type(message), type(info)])
))
# girl_2.working()
print('\n')


# Множественное наследование
# class Father:
#     def send_money(self):
#         print('Деньги перечислены')
#
#     def my_dream(self):
#         print('Я стану космонавтом')


class Mother:
    def be_happy(self):
        print('Не в деньгах счастье! А в их количестве ))')

    def my_dream(self):
        print('Где спрятаться от этого всего!')


# Полиморфизм | Перегрузка методов
class Father:
    def send_money(self, empty: bool = False):
        if not empty:
            print('Деньги перечислены')
        else:
            print('Я иду заработать')


class Child(Mother, Father):
    def my_dream(self):
        print('Закончу школу и жизнь изменится ^_^')


baby = Child()
baby.send_money()
baby.send_money(empty=True)
baby.be_happy()
baby.my_dream()
print('\n')

print('the end')

