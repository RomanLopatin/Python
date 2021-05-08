"""coding=utf-8
6.1.3 (через counter)
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
(берем задачу 3.4: Определить, какое число в массиве встречается чаще всего.)
"""
# Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32

import sys
import random
import collections

memory_count = 0  # здесь будем считать память

ARR_SIZE = 10
el_min = 0
el_max = 10

counter = collections.Counter()

for el in [random.randint(el_min, el_max) for _ in range(ARR_SIZE)]:
    counter[el] += 1
    ############
    memory_count += sys.getsizeof(el)
    ############

most_common = counter.most_common(1)[0]
############
memory_count += (sys.getsizeof(ARR_SIZE) + sys.getsizeof(el_min)
                 + sys.getsizeof(counter) + sys.getsizeof(most_common))
############
print(counter)
print(f'Чаще всего встречается число {most_common[0]} - {most_common[1]} раза')
print(f'Нужно памяти: {memory_count} байт')

# Варант программы через коллекцию Counter - оптимальный! Затраты оперативной памяти - около 760 байт
# Выигрыш по сравнению с двумя другими варантами - почти в 2 раза!
