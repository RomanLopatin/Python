"""coding=utf-8
7.2
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы.
"""
import random


def sort_merge(arr):
    # print(arr)
    if len(arr) > 2:
        div_el = len(arr) // 2
        arr_1 = sort_merge(arr[:div_el])
        arr_2 = sort_merge(arr[div_el:])
    else:
        arr_1 = arr[:1]
        arr_2 = arr[1:]
    # print(arr_1, arr_2)
    res = [0] * len(arr)
    i = j = k = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            res[k] = arr_1[i]
            i += 1
        else:
            res[k] = arr_2[j]
            j += 1
        k += 1
    while i < len(arr_1):
        res[k] = arr_1[i]
        i += 1
        k += 1
    while j < len(arr_2):
        res[k] = arr_2[j]
        j += 1
        k += 1
    return res


num = 10
max_ = 50
array = [random.random()*max_ for i in range(num)]
# array = [5, 7, 2, 1, 3, 0, 3, 9, 3]
print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {sort_merge(array)}')
