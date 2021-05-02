""""
coding=utf-8
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
from random import randint



class Car:
    speed = 0
    speed_lim = None
    color = ""
    name = ""
    is_police = bool

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self):
        print("машина повернула")

    def show_speed(self):
        print(f"Ваша скорость: {self.speed}")

    def speed_generator(self):
        return randint(0, 120)


class TownCar(Car):
    def __init__(self):
        self.is_police = False
        self.speed_lim = 60
        self.name = "Городская машина"

    def show_speed(self):
        if self.speed > self.speed_lim:
            print(f"Ваша скорость: {self.speed}. Превышение!")
        else:
            print(f"Ваша скорость: {self.speed}.")


class WorkCar(Car):
    def __init__(self):
        self.is_police = False
        self.speed_lim = 40
        self.name = "Рабочая машина"

    def show_speed(self):
        if self.speed > self.speed_lim:
            print(f"Ваша скорость: {self.speed}. Превышение!")
        else:
            print(f"Ваша скорость: {self.speed}.")


class SportCar(Car):
    def __init__(self):
        self.is_police = False
        self.name = "Спортивная машина"


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True
        self.name = "Полицейская машина"


# my_car = Car()
# my_car.speed = 100
# my_car.show_speed()

my_car = TownCar()
my_car.speed = my_car.speed_generator()
print(my_car.name)
my_car.show_speed()
print(f"Это полиция? {my_car.is_police}")
#
my_car = SportCar()
my_car.speed = my_car.speed_generator()
print(my_car.name)
my_car.show_speed()
print(f"Это полиция? {my_car.is_police}")
#
my_car = WorkCar()
my_car.speed = my_car.speed_generator()
print(my_car.name)
my_car.show_speed()
print(f"Это полиция? {my_car.is_police}")
#
my_car = PoliceCar()
my_car.speed = my_car.speed_generator()
print(my_car.name)
my_car.show_speed()
print(f"Это полиция? {my_car.is_police}")
