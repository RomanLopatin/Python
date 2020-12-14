""""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
try:
    with open("my_file.txt", "r") as my_file_obj:
        str_count = 0
        money_count = 0
        money_limit = 20000

        for line in my_file_obj:
            Person_data_list = line.split()
            try:
                if float(Person_data_list[1]) < money_limit:
                    print(f"{Person_data_list[0]} - {Person_data_list[1]}")
                str_count += 1
                money_count += float(Person_data_list[1])
            except IndexError:
                print("Ошибка чтения файла")
        print(f"Средннй доход сотрудников: {round(money_count / str_count, 2)}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
