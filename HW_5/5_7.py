""""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json


firm_list = []
firm_dict = dict()
avrg_prof_dict = dict()
accum_profit = 0
firm_counter = 0
try:
    with open("companies_info.txt", encoding='UTF-8') as obj_file:
        try:
            for line in obj_file:
                firm_info = line.split("   ", 2)
                name = firm_info[0]
                fin_data = list(map(float, firm_info[2].split()))
                profit = fin_data[0] - fin_data[1]
                firm_dict[name] = profit
                if profit > 0:
                    accum_profit += profit
                    firm_counter += 1
            firm_list.append(firm_dict)
            try:
                avrg_prof_dict["average_profit"] = accum_profit / firm_counter
            except ZeroDivisionError:
                avrg_prof_dict["average_profit"] = 0
            firm_list.append(avrg_prof_dict)
            print(firm_list)
        except IndexError:
            print("Ошибка формата файла!")
except FileNotFoundError:
    print("Файл не найден!")
with open("my_file.json", "w") as write_jsf:
    json.dump(firm_list, write_jsf)
