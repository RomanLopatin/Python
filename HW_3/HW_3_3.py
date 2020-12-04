"""
3.Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

"""


def my_func(a, b, c):
    try:
        return float(a) + float(b) + float(c) - min(float(a), float(b), float(c))
    except ValueError:
        return "Ошибка ввода данных!"


print(my_func(input("Введите первое число: "),
              input("Введите второе число: "),
              input("Введите третье число: ")))
