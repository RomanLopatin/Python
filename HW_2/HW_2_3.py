""""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

list_months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
list_seasons = ["winter", "spring", "summer", "autumn"]
dict_seasons = {0: "winter", 1: "spring", 2:"summer", 3: "autumn"}

my_month = input("Введите номер месяца (1-12): ")
if my_month.isdigit() and 0 < int(my_month) <= 12:
    my_month_int = int(my_month)
    # !!!Выражение (my_month_int %12) в строке ниже нужно для корректной обработки декабря (месяца 12)!!!
    print(f"Через список: {list_months[my_month_int - 1]} is {list_seasons[(my_month_int % 12) // 3]}")
    print(f"Через словарь: {list_months[my_month_int - 1]} is {dict_seasons[(my_month_int % 12) // 3]}")
