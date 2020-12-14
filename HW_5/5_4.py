""""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

try:
    with open("counter.txt", "r") as my_file_obj:
        for line in my_file_obj:
            line_list = line.split("-")
            line_word = line_list[0]
            print(line_word)
            new_f = open("out_file_"+line_word + ".txt", "w")
            new_f.write(line_word)
            new_f.close()
except IOError:
    print("Ошибка чтения файла")