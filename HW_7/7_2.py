""""coding=utf-8
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Closes(ABC):
    total_fabric = 0

    def __init__(self, size):
        self.size = size

    def fabric_count(self, fabric):
        Closes.total_fabric += fabric

    @abstractmethod
    def fabric_calc(self):
        pass


class Coat(Closes):
    def __init__(self, size):
        super().__init__(size)
        super().fabric_count(self.fabric_calc)
        #  !!!Вопрос: Можно ли напрямую обратиься к атттрибуту total_fabric без вызова функции?
        # типа super().total_fabric += self.fabric.calc?

    @property
    def fabric_calc(self):
        return self.size / 6.5 + 0.5


class Costume(Closes):
    def __init__(self, size):
        super().__init__(size)
        super().fabric_count(self.fabric_calc)

    @property
    def fabric_calc(self):
        return self.size * 2 + 0.3


a = Coat(6.5)
print(a.fabric_calc)
print(Closes.total_fabric)
b = Costume(2)
print(b.fabric_calc)
print(Closes.total_fabric)
print(Coat.total_fabric)
