"""
coding=utf-8
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
 программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class MyZeroDivisionError(Exception):
    def __init__(self, msg):
        pass


a = input("Ввелите делимое : ")
b = input("Ввелите делитель: ")

try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise MyZeroDivisionError("На ноль делить нельзя!")
    c = a / b
    print(f"{a}/{b}={c}")
except ValueError:
    print("Вводимые данные должны быть числами!")
except MyZeroDivisionError as err:
    print(err)
