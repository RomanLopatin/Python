"""coding=utf-8
3.6.
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

arr_size = 10
range_min = 0
range_max = 100

ind_max = 0
ind_min = 0

arr = [random.randint(range_min, range_max) for _ in range(arr_size)]
print(f'old: {arr}')

el_max = arr[0]
el_min = arr[0]

for i in range(1, arr_size):

    if arr[i] > el_max:
        el_max = arr[i]
        ind_max = i

    if arr[i] < el_min:
        el_min = arr[i]
        ind_min = i

print(f'Мин: {el_min} / Max: {el_max}')

sum = 0

if ind_min>ind_max:
    ind_min, ind_max = ind_max, ind_min

for i in range(ind_min + 1, ind_max):
    sum += arr[i]

print(f'Сумму искомых элементов: {sum}')
