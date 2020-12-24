"""
coding=utf-8
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class IsNotANumberError(Exception):
    def __init__(self, msg):
        pass


our_list = []
print("Введите элементы списка (числа): (чтобы закончить ввод списка - просто нажмите клавишу 'Enter')")
while True:
    el = input("новый элемент:")
    if el == "":
        break
    try:
        if not el.isnumeric():
            raise IsNotANumberError("Ошибка ввода! Нужно вводить числа!")
    except IsNotANumberError as err:
        print(err)
    else:
        our_list.append(int(el))
print(f"Итоговый список: {our_list}")