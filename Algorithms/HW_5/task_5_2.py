"""coding=utf-8
5.2.
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import namedtuple

Num_16 = namedtuple('Num_16', 'Val')


def total_sum_16(n1, n2):
    list_16 = list('0123456789ABCDEF')
    len_1 = len(n1)
    len_2 = len(n2)

    if len_1 < len_2:
        n1 = ['0'] * (len_2 - len_1) + n1
        len_max = len_2
    else:
        n2 = ['0'] * (len_1 - len_2) + n2
        len_max = len_1

    res = []
    tail = "0"
    for ind in range(len_max - 1, -1, -1):
        raw_index = list_16.index(n1[ind]) + list_16.index(n2[ind]) + list_16.index(tail)
        res = [list_16[raw_index % 16]] + res
        tail = list_16[raw_index // 16]
    if tail != "0":
        res = tail + res
    return res


x = Num_16(list(input('Введите первое число:')))
y = Num_16(list(input('Введите второе число:')))
print(f'{x.Val}+{y.Val} = {total_sum_16(x.Val, y.Val)}')

