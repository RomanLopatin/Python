""""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
count_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
our_split = " - "
try:
    with open("counter.txt", "r") as my_file_obj:
        for line in my_file_obj:
            line_list = line.split(our_split)
            line_word = line_list[0]
            line_digit = line_list[1]
            try:
                new_f = open("out_file_" + line_word + ".txt", "w")
                new_f.write(count_dict.get(line_word) + our_split + line_digit)
            except TypeError:
                print("Ошибка преобразования типа!")
            except IOError:
                print("Ошибка ввода-вывода!")
            finally:
                new_f.close()
except IOError:
    print("Ошибка чтения файла!")
