""""coding=utf-8
1.9
ПВводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
print('Введите 3 числа: a,b,c')
a = float(input('Введите a:'))
b = float(input('Введите b:'))
c = float(input('Введите c:'))

if a > b:
    if a < c:
        print(f"Среднее число - {a}")
    else:
        if b < c:
            print(f"Среднее число - {c}")
        else:
            print(f"Среднее число - {b}")
else:
    if a > c:
        print(f"Среднее число - {a}")
    else:
        if b < c:
            print(f"Среднее число - {b}")
        else:
            print(f"Среднее число - {c}")
