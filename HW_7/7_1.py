""""
coding=utf-8
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


#  !!!Вопрос:  Наверное эту функцию надо бы оформить через метод __new__() нашего класса, но не соображу как это сделать?
def new_matrix(m, n):
    return [[int(input(f"Введите элемент матрицы {i + 1, j + 1}: ")) for j in range(n)] for i in range(m)]


class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        our_str = ""
        for line in self.my_matrix:
            our_str += " ".join(str(line)) + "\n"
        return our_str

    def __add__(self, other):
        m1 = self.my_matrix
        m2 = other.my_matrix
        m3 = [[m1[i][j] + m2[i][j] for j in range(2)] for i in range(2)]
        return Matrix(m3)
    #
    #   !!!Еще вопрос. Результат сложения объектов класса должен быть объект того же класса что и слагаемые или нет?
    #   !!!Я проверил пример метода __add__, что Вы дали на занятии - там результат сложения имеет <class 'str'>.
    # def __add__(self, other):
    #     c = []
    #     for i in range(len(self.my_matrix)):
    #         c.append([])
    #         for j in range(len(self.my_matrix[0])):
    #             c[i].append((self.my_matrix[i][j] + other.my_matrix[i][j]))
    #     return "\n".join(map(str, c))


m_1 = Matrix(new_matrix(2, 2))
print(m_1)
m_2 = Matrix(new_matrix(2, 2))
print(m_2)
m_3 = m_1 + m_2
print(m_3)
print(type(m_3))