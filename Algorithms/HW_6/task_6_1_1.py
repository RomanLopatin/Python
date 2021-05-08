"""coding=utf-8
6.1.1 (через список)
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

list_ = [random.randint(el_min, el_max) for _ in range(ARR_SIZE)]
############
memory_count += sys.getsizeof(ARR_SIZE) + sys.getsizeof(el_min) + sys.getsizeof(list_)
# здесь пока учитываем только память под структуру списка,
# память под объекты списка учтем через множество, поскольку элементы списка могут повторяться
# ARR_SIZE = 10 и el_max = 10. Учитываем 1 раз.
############

set_ = set(list_)
############
memory_count += sys.getsizeof(set_)
############
top_el = list_[0]
top_count = 0
for el in set_:
    el_count = 0
    for i in range(ARR_SIZE):
        if list_[i] == el:
            el_count += 1
    if el_count > top_count:
        top_el = el
        top_count = el_count
    ############
    memory_count += sys.getsizeof(el)  # здесь учитываем учитываем память под сами элементы
    ############
############
memory_count += sys.getsizeof(el_count) + sys.getsizeof(i) + sys.getsizeof(top_el) + sys.getsizeof(top_count)
############
print(list_)
print(f'Чаще всего встречается число {top_el} ({top_count} раза)')
print(f'Нужно памяти: {memory_count} байт')

# Исходный варант программы (через список) наиболее требовательный по памяти - около 1270 байт
