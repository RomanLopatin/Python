""""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
my_dict = dict()
with open("Curriculum.txt") as my_file_obj:
    for line in my_file_obj:
        line_list = line.split(":", 1)
        # name, rest = line.split(":")
        list_quant = (line_list[1].split())
        subj_hours = 0
        for el in list_quant:
            try:
                subj_hours += float(el.split("(", 1)[0])
            except:
                pass
        my_dict[line_list[0]] = subj_hours
    print(my_dict)
