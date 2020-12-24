"""
coding=utf-8
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class ClsData:
    def __init__(self, data_str):
        self.data_tup = ClsData.data_validation(ClsData.data_into_int(data_str))

    def __str__(self):
        return str(self.data_tup)

    @classmethod
    def data_into_int(cls, data_str):
        try:
            data_int = tuple([int(el) for el in data_str.split("-")])
            return data_int
        except ValueError:
            print(f"Введены некорректные данные! ({data_str} не удалось преобразовать к типу «число»)")
            return 0, 0, 0

    @staticmethod
    def data_validation(data_tup):

        if data_tup == (0, 0, 0):
            return 0, 0, 0

        data_day = data_tup[0]
        data_month = data_tup[1]
        data_year = data_tup[2]

        month_is_correct = data_month in range(1, 12)
        year_is_correct = data_year in range(1, 2099)
        leap_year = (data_year % 4 == 0 and data_year % 100 != 0) or (data_year % 400 == 0 and data_year % 100 == 0)

        if month_is_correct and year_is_correct:
            date_is_correct = (data_month in {1, 3, 5, 7, 8, 10, 12} and data_day in range(1, 31 + 1)) \
                              or (data_month in {4, 6, 9, 11} and data_day in range(1, 30 + 1)) \
                              or (data_month == 2 and leap_year and data_day in range(1, 29 + 1)) \
                              or (data_month == 2 and not leap_year and data_day in range(1, 28 + 1))
        else:
            date_is_correct = False

        if date_is_correct:
            print(f"Дата {data_tup} введена корректно!")
            return data_tup
        else:
            print(f"Дата {data_tup} введена некорректно!")
            return 0, 0, 0


obj_data = ClsData("29-02-20f1")
print(obj_data)
obj_data = ClsData("29-02-2001")
print(obj_data)
obj_data = ClsData("29-02-2000")
print(obj_data)
obj_data = ClsData("30-13-2000")
print(obj_data)
obj_data = ClsData("22-02-20010")
print(obj_data)
obj_data = ClsData("31-11-2000")
print(obj_data)
obj_data = ClsData("31-12-2000")
print(obj_data)
#
