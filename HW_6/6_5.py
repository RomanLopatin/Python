""""
coding=utf-8
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery():
    title = ""

    def draw(self):
        print("Запуск отрисовки - ручка.")


class Pen(Stationery):
    def __init__(self):
        self.title = "ручка"

    def draw(self):
        print(f"Запуск отрисовки - {self.title}")


class Pencil(Stationery):
    def __init__(self):
        self.title = "карандаш"

    def draw(self):
        print(f"Запуск отрисовки - {self.title}")


class Handle(Stationery):
    def __init__(self):
        self.title = "маркер"

    def draw(self):
        print(f"Запуск отрисовки - {self.title}")


my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
