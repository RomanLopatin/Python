"""
coding=utf-8
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
 сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
 и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class IsNotANumberError(Exception):
    def __init__(self, msg):
        pass


class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        try:
            if (type(self.a) == int or type(self.a) == float) and (type(self.b) == int or type(self.b) == float):
                pass
            else:
                raise IsNotANumberError("Ошибка ввода данных!")
        except IsNotANumberError as err:
            self.a = 0
            self.b = 0
            print(err)


    def __str__(self):
        self_bxi = "" if self.b == 0 else "i" if abs(self.b == 1) else str(abs(self.b)) + "i"
        return f"{self.a if self.a != 0 else ''} {'+' if self.b > 0 else '-' if self.b < 0 else ''} " \
               f"{'' if self.b == 0 else 'i' if abs(self.b) == 1 else str(abs(self.b)) + 'i'}"

    def __add__(self, other):
        return ComplexNumbers(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumbers(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return ComplexNumbers(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


z1 = ComplexNumbers("d", -1)
z2 = ComplexNumbers(1, -1)
z3 = z1 + z2
print(z1, z2, z3)
print(z1 * z2)
