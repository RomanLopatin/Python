""""
coding=utf-8
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        # self.name = name
        # self.surname = surname
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


pos1 = Position()
pos1.name = input("Введите имя сотрудника: ")
pos1.surname = input("Введите фамилию сотрудника: ")
pos1._income["wage"] = int(input("Введите оклад сотрудника: "))
pos1._income["bonus"] = int(input("Введите премию сотрудника: "))
print(f"Атрибуты сотрудника: {pos1.name}, {pos1.surname},{pos1._income}")
print(f"Вызов метода get_full_name(): {pos1.get_full_name()}")
print(f"Вызов метода get_total_income() {pos1.get_total_income()}")
