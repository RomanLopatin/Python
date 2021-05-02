"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
# Для вызова скрипта в терминале вводим строку:"python salary_calc_script.py <hours> <hour_payment> <bonus>"
from sys import argv


def salary_calc(hour_payment, hours, bonus):
    try:
        return float(hour_payment) * float(hours) + float(bonus)
    except ValueError:
        return "Ошибка ввода данных!"


script_name, hour_payment, hours, bonus = argv
print(f"Зарплата сотрудника: {salary_calc(hour_payment, hours, bonus)}")
