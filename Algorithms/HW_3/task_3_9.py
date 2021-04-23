"""coding=utf-8
3.9.
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

arr_size_1 = 3
arr_size_2 = 2
range_min = 0
range_max = 100

ind_max = 0
ind_min = 0

arr = [[random.randint(range_min, range_max) for _ in range(arr_size_1)] for _ in range(arr_size_2)]

print(f'arr: {arr}')

min_arr = []
for j in range(arr_size_1):
    spam_min = range_max
    for i in range(arr_size_2):
        if arr[i][j] < spam_min:
            spam_min = arr[i][j]
    min_arr.append(spam_min)

print(f'arr_min: {min_arr}')

arr_max = range_min
for i in range(arr_size_1):
    if min_arr[i] > arr_max:
        arr_max = min_arr[i]

print(f'arr max: {arr_max}')