""""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce


def my_sum_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


our_number_list = ("1 3 65 345 34 23 44 34 34").split()
print("Исходный список: ", our_number_list)
our_file = "new_file.txt"
#  Запись файла
try:
    with open(our_file, "w") as f_obj:
        for el in our_number_list:
            f_obj.write(el + " ")
except IOError:
    print("Ошибка ввода-вывода!")

#  Чтение файла и подсчет
try:
    with open(our_file, "r") as f_obj:
        print(f"Сумма чисел равна: {sum(list(map(float, f_obj.readline().split())))}")
except IOError:
    print("Ошибка ввода-вывода!")
except ValueError:
    print("Ошибка преобразования типа!")
except NameError:
    print("Файл не обнаружен!")
