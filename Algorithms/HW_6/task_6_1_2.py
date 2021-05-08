"""coding=utf-8
6.1.2 (через кортеж)
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
(берем задачу 3.4: Определить, какое число в массиве встречается чаще всего.)
"""
# Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32

import sys
import random

memory_count = 0  # здесь будем считать память

ARR_SIZE = 10
el_min = 0
el_max = 10

tuple_ = tuple(random.randint(el_min, el_max) for _ in range(ARR_SIZE))
############
memory_count += sys.getsizeof(ARR_SIZE) + sys.getsizeof(el_min) + sys.getsizeof(tuple_)
# здесь пока учитываем только память под структуру кортежа,
# память под его объекты учтем через множество,дабы избежать двойного учета
# ARR_SIZE = 10 и el_max = 10.  Учитываем 1 раз.
############

set_ = set(tuple_)
############
memory_count += sys.getsizeof(set_)
############

top_el = tuple_[0]
top_count = 0

for el in set_:
    el_count = 0
    for item in tuple_:
        if item == el:
            el_count += 1
    if el_count > top_count:
        top_el = el
        top_count = el_count
    ############
    memory_count += sys.getsizeof(el)  # здесь учитываем учитываем память под сами элементы
    ############
############
memory_count += sys.getsizeof(el_count) + sys.getsizeof(item) + sys.getsizeof(top_el) + sys.getsizeof(top_count)
############
print(tuple_)
print(f'Чаще всего встречается число {top_el} ({top_count} раза)')
print(f'Нужно памяти: {memory_count} байт')

# Варант программы через кортеж чуть менее прожорливый - около 1230 байт

