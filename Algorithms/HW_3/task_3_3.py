"""coding=utf-8
3.3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
arr[ind_max], arr[ind_min] = arr[ind_min], arr[ind_max]

print(f'new: {arr}')
