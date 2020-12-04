"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func_positive(x, n):
    return x if n == 1 else my_func_positive(x, n - 1) * x


def my_func_negative(x, n):
    return 1 / x if n == -1 else my_func_negative(x, n + 1) / x


def my_func(x, n):
    if n > 0:
        return my_func_positive(x, n)
    elif n < 0:
        return my_func_negative(x, n)
    else:
        return 1


print("Результат возведения в степень: ",
      my_func(float(input("Введите основание (положительное число): ")),
              int(input("Введите показатель степени (целое число): "))))
