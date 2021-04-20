""""coding=utf-8
1.1
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
abc = int(input('Введите 3-х значное число:'))
a = abc//100
b = (abc - a*100)//10
c = abc - a*100 - b*10
print(f'a+b+c = {a+b+c}')
print(f'a*b*c = {a*b*c}')

""""
ссылка на блок-схемы
https://drive.google.com/file/d/1ke7NWG_u5Ea52qj6U8raal6-xY_BCTL6/view?usp=sharing
"""