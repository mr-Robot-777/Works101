import cProfile
import timeit
import sys

sys.setrecursionlimit(150000)



def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

def func(n):
    b = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            b.append(i)
    return b


print('\nВремя на решете Эратосфена: ', timeit.timeit(f'eratosthenes(1000)', setup='from __main__ import eratosthenes', number=100))
print('Время на обычной функции: ', timeit.timeit(f'func(1000)', setup='from __main__ import func', number=100), '\n')

print('решето Эратосфена:\n')
cProfile.run("eratosthenes(10000)")
print('Функция:\n')
cProfile.run("func(10000)")


# Вывод:




# """
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
#
# Подсказка:
# Сравните алгоритмы по времени на разных порядковых номерах чисел:
# 10, 100, 1000
# Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
# Подумайте и по возможности определите сложность каждого алгоритма
#
# ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
# БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
# """
#
#
# import timeit
#
#
# def eratosthenes(n):
#     sieve = list(range(n + 1))
#     sieve[1] = 0
#     for i in sieve:
#         if i > 1:
#             for j in range(i + i, len(sieve), i):
#                 sieve[j] = 0
#     return sieve
#
# def func(n):
#     b = []
#     for i in range(2, n):
#         result = True
#         for j in range(2, i):
#             if i % j == 0:
#                 result = False
#         if result:
#             b.append(i)
#     return b
#
#
# print('\nВремя на решете Эратосфена(10): ', timeit.timeit(f'eratosthenes(10)', setup='from __main__ import eratosthenes', number=100))
# print('Время на обычной функции(10): ', timeit.timeit(f'func(10)', setup='from __main__ import func', number=100), '\n')
#
# print('\nВремя на решете Эратосфена(100): ', timeit.timeit(f'eratosthenes(100)', setup='from __main__ import eratosthenes', number=100))
# print('Время на обычной функции(100): ', timeit.timeit(f'func(100)', setup='from __main__ import func', number=100), '\n')
#
# print('\nВремя на решете Эратосфена(1000): ', timeit.timeit(f'eratosthenes(1000)', setup='from __main__ import eratosthenes', number=100))
# print('Время на обычной функции(1000): ', timeit.timeit(f'func(1000)', setup='from __main__ import func', number=100), '\n')
#
#
#
# # Мои данные:
# # Время на решете Эратосфена(10):  0.00022344199987855973
# # Время на обычной функции(10):  0.0003820070000983833
# #
# #
# # Время на решете Эратосфена(100):  0.0016190349999760656
# # Время на обычной функции(100):  0.02820273899988024
# #
# #
# # Время на решете Эратосфена(1000):  0.021256588000142074
# # Время на обычной функции(1000):  2.4750579080000534
# #
# # Вывод: При увеличении входных данных значительно увеличивается время выполнения функции в то время как решето Эратосфена увеличивается не столь быстро.
# #