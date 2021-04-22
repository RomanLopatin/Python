""""coding=utf-8
2.2
 Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = int(input("Введите натуральное число:"))

odd_count = 0
even_count = 0

while True:
    dig = num % 10
    if dig % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10
    if num == 0:
        break
print(f'четных - {even_count}/нечетных - {odd_count}')

"""
Ссылка на диаграммы к дом. заданию 2:
https://drive.google.com/file/d/19v8_80g4Pl4SYY345Jnb59lLkKnVHiFR/view?usp=sharing
"""
