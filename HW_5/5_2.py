"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
"""

try:
    with open("my_file.txt", "r") as my_file_obj:
        str_counter = 0

        for line in my_file_obj:
            str_counter += 1
            print(line, end='')
            print(f"Cлов в строке {str_counter}: {len(line.split())} \n")
        print(f"В файле строк: {str_counter}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
