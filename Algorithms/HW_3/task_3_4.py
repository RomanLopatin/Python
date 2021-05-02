"""coding=utf-8
3.4.
Определить, какое число в массиве встречается чаще всего.
"""

import random

arr_size = 10
el_min = 0
el_max = 10

arr = [random.randint(el_min, el_max) for _ in range(arr_size)]
print(arr)

top_el = arr[0]
top_count = 0

set_ = set(arr)
for el in set_:
    el_count = 0
    for i in range(arr_size):
        if arr[i] == el:
            el_count += 1
    if el_count > top_count:
        top_el = el
        top_count = el_count

print(f'Чаще всего встречается число {top_el} ({top_count} раза)')
