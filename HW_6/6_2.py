""""
coding=utf-8
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    #  аттрибуты класса
    _mass_per_sq = 25  # (масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см)
    _road_thick = 5  # (см.)

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def road_mass_calc(self):
        return print(
            f"Масса дороги составит: {self._length * self._width * self._mass_per_sq * self._road_thick / 1000} т")


my_road = Road(10, 20)
my_road.road_mass_calc()
