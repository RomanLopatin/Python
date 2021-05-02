"""coding=utf-8
3.8.
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

arr_size = 10
range_min = 0
range_max = 10

arr = [random.randint(range_min, range_max) for _ in range(arr_size)]
#  arr = [13, 51, 41, 81, 28, 66, 82, 27, 82, 56]
print(f'arr: {arr}')

ind_min = 0
el_min = arr[ind_min]

for i in range(1, arr_size):

    if arr[i] < el_min:
        el_min = arr[i]
        ind_min = i

print(f'минимум = {el_min}, его индекс - {ind_min}')

ind_min_2 = 1
el_min_2 = arr[ind_min_2]

for i in range(0, arr_size):

    if arr[i] < el_min_2 and i != ind_min:
        el_min_2 = arr[i]
        ind_min_2 = i

    if el_min_2 == el_min:
        break

print(f'минимум 2 = {el_min_2}, его индекс - {ind_min_2}')
