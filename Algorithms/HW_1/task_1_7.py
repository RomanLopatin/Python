""""coding=utf-8
1.7
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним..
"""
print('Введите длины 3-х отрезков: a,b,c.')
a = float(input('Введите a:'))
b = float(input('Введите b:'))
c = float(input('Введите c:'))
if a + b > c and a + c > b and b + c > a:

    print("Треугольник возможен!")
    if a == c or a == b or b == c:
        if a == c and b == c:
            print("Треугольник равноcторонний!")
        else:
            print("Треугольник равнобедренный!")
    else:
        print("Треугольник разносторонний!")
else:
    print("Треугольник не возможен!")
