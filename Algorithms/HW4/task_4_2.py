"""coding=utf-8
4.2.
"""
import timeit
import cProfile

HOLE = 0
N = 1000


def erat_alg(N, HOLE):
    sieve = [i for i in range(N)]
    sieve[1] = HOLE
    for i in range(2, N):
        if sieve[i] != HOLE:
            j = i + i
            while j < N:
                sieve[j] = HOLE
                j += i

    res_1 = [item for item in sieve if item != HOLE]
    return res_1


def check_alg(N):
    res_2 = list()
    res_2.append(2)
    for i in range(2, N):
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                res_2.append(i)
    return res_2


# print(erat_alg(N, HOLE))
# print(check_alg(N))

print(timeit.timeit('erat_alg(100, 0)', number=100, globals=globals()))  # 0,0045083
print(timeit.timeit('erat_alg(200, 0)', number=100, globals=globals()))  # 0,009767
print(timeit.timeit('erat_alg(400, 0)', number=100, globals=globals()))  # 0,0210418
print(timeit.timeit('erat_alg(800, 0)', number=100, globals=globals()))  # 0,0354941
print(timeit.timeit('erat_alg(1600, 0)', number=100, globals=globals()))  # 0,0832306
print('-----------------------------------------------------------------')
print(timeit.timeit('check_alg(100)', number=100, globals=globals()))  # 0,0139173
print(timeit.timeit('check_alg(200)', number=100, globals=globals()))  # 0,0622221
print(timeit.timeit('check_alg(400)', number=100, globals=globals()))  # 0,2135938
print(timeit.timeit('check_alg(800)', number=100, globals=globals()))  # 0,8175896
print(timeit.timeit('check_alg(1600)', number=100, globals=globals()))  # 3,2337362

cProfile.run('erat_alg(1600, 0)')
cProfile.run('check_alg(1600)')

#  Вывод: Решето Эратосфена много эффективней провеки делимости через полный перебор!
# Решето Эратосфена напоминает линейную ассимптоику, в то время как перебор - растет экспоненциально
#  ссылка на график: https://drive.google.com/file/d/16Q4lts5Kw_itujRujChg-6HAfq27q04Q/view?usp=sharing
