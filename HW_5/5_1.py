""""
coding=utf-8
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

with open("my_file_.txt", "w") as my_file_obj:
    while True:
        new_str = input("Введите новую строку: ")
        if new_str != "":
            my_file_obj.write(new_str+"\n")
        else:
            break


