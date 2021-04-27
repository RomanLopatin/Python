"""coding=utf-8
4.1.(2.4.)
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
import timeit
import cProfile

# N = int(input("Введите натуральное число:"))
ELEM_ = 1
STEP_ = -0.5


# способ 1
def variant_1(n, elem_=ELEM_, step_=STEP_):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += elem_
        elem_ *= step_
    return sum_


# способ 2
def variant_2(n, elem_=ELEM_, step_=STEP_):
    sum_ = 0
    i = 0
    while i < n:
        sum_ += elem_
        elem_ *= step_
        i += 1
    return sum_


# способ 3
def variant_3(N, elem_=ELEM_, step_=STEP_):
    def rec_count(n=N, el_=elem_, st_=step_):
        if n == 1:
            return el_
        else:
            return el_ + rec_count(n - 1, el_ * st_)

    return rec_count(N)


# print(f'Сумма {N} элементов ряда равна {variant_1(N)}')
# print(f'Сумма {N} элементов ряда равна {variant_2(N)}')
# print(f'Сумма {N} элементов ряда равна {variant_3(N)}')


print(timeit.timeit('variant_1(10,1,-0.5)', number=100, globals=globals()))  # 0.0003270000000000009
print(timeit.timeit('variant_1(20,1,-0.5)', number=100, globals=globals()))  # 0.0008032999999999998
print(timeit.timeit('variant_1(40,1,-0.5)', number=100, globals=globals()))  # 0.0007817999999999992
print(timeit.timeit('variant_1(80,1,-0.5)', number=100, globals=globals()))  # 0.0010024000000000005
print(timeit.timeit('variant_1(160,1,-0.5)', number=100, globals=globals()))  # 0.0024585999999999983
print(timeit.timeit('variant_1(320,1,-0.5)', number=100, globals=globals()))  # 0.004584899999999996
print("-------------------------------------------------------------------")
print(timeit.timeit('variant_2(10,1,-0.5)', number=100, globals=globals()))  # 0.00015620000000000217
print(timeit.timeit('variant_2(20,1,-0.5)', number=100, globals=globals()))  # 0.00028840000000000116
print(timeit.timeit('variant_2(40,1,-0.5)', number=100, globals=globals()))  # 0.0005577999999999972
print(timeit.timeit('variant_2(80,1,-0.5)', number=100, globals=globals()))  # 0.0017588000000000048
print(timeit.timeit('variant_2(160,1,-0.5)', number=100, globals=globals()))  # 0.0031543000000000126
print(timeit.timeit('variant_2(320,1,-0.5)', number=100, globals=globals()))  # 0.006486499999999992
print("-------------------------------------------------------------------")
print(timeit.timeit('variant_3(10,1,-0.5)', number=100, globals=globals()))  # 0.0002485000000000126
print(timeit.timeit('variant_3(20,1,-0.5)', number=100, globals=globals()))  # 0.00041940000000000033
print(timeit.timeit('variant_3(40,1,-0.5)', number=100, globals=globals()))  # 0.0013814999999999938
print(timeit.timeit('variant_3(80,1,-0.5)', number=100, globals=globals()))  # 0.0028892999999999974
print(timeit.timeit('variant_3(160,1,-0.5)', number=100, globals=globals()))  # 0.005201899999999995
print(timeit.timeit('variant_3(320,1,-0.5)', number=100, globals=globals()))  # 0.0087314
print("-------------------------------------------------------------------")
cProfile.run('variant_1(9900,1,-0.5)')  # 4 function calls in 0.001 seconds
cProfile.run('variant_2(9900,1,-0.5)')  # 4 function calls in 0.002 seconds
cProfile.run('variant_3(990,1,-0.5)')  # 994 function calls (5 primitive calls) in 0.003 seconds

#  Вывод: любой из вариантов с циклом существенно быстрее рекурссии при больших N.
#  С ростом N разрыв увеличивается
#  Цикл 'for' - быстрее цикла 'while'.
#  Все варианты похожи на степенную ассимптотику, при чем вариант с рекурсией растет быстрее всего
#  ссылка на график: https://drive.google.com/file/d/16Q4lts5Kw_itujRujChg-6HAfq27q04Q/view?usp=sharing
