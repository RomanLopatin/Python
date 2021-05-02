"""coding=utf-8
5.1.
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

quarter_num = 4
Company = namedtuple('Company', 'Name, profit')  # структура для хранения названия компании и квартальных прибылей

co_arr = []  # массив для Company
total_profit = 0

N = int(input("Введите число компаний:"))

for i in range(N):  # в цикле заполняем данные по всем N компаниям
    spam_name = str(input("Введите название компании:"))
    spam_profit = []
    for q in range(quarter_num):  # в цикле заполняем массив поквартальных прибылей i-й компании
        spam_profit.append(float(input(f"Прибыль за {q + 1}-й квартал:")))
    co_arr.append(Company(spam_name, spam_profit))
    total_profit += sum(spam_profit)

average_profit = total_profit / N

above_co = []
below_co = []
for i in range(N):  # в цикле формируем 2 массива компаний, в соответствии с прибылью
    if sum(co_arr[i].profit) >= average_profit:  # прим.: в этот список попадают фирмы, чья прибыль НЕ НИЖЕ средней
        above_co.append(co_arr[i].Name)
    else:
        below_co.append(co_arr[i].Name)

print(f'Средняя прибыль предприятий: {average_profit}')
print('Предприятия, чья прибыль выше (или равно) среднего:')
for el in above_co:
    print(el)
print('Предприятия, чья прибыль ниже среднего:')
for el in below_co:
    print(el)
