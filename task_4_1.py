# Выбрал 5 задание к 3 уроку
# В массиве найти максимальный отрицательный элемент и вывести на экран его значение и позицию в массиве.
# Все алгоритмы имеют линейную сложность. Алгоритм с циклом while оказывается медленее остальных
# Чуть быстрее остальных является алгоритм с созданием массива без положительных чисел и нахождения
# максимального отрицательного числа через max, а затем уже по этому числу ищется его индекс в первоначальном массиве

import random
import cProfile
import timeit


def my_array(size):
    MIN_ITEM = -10
    MAX_ITEM = 10
    array = [random.randint(MIN_ITEM * size, MAX_ITEM * size) for _ in range(size)]
    return array


def my_func(num_list):
    i = 0
    index = -1
    while i < len(num_list):
        if num_list[i] < 0 and index == -1:
            index = i
        elif num_list[index] < num_list[i] < 0:
            index = i
        i += 1
    return f'В массиве: \n{num_list} \nминимальный отрицательный элемент = {num_list[index]} \nего индекс = {index}'


print(timeit.timeit('my_func(my_array(10))', number=100, globals=globals()))        #0.0012233999999999995
print(timeit.timeit('my_func(my_array(100))', number=100, globals=globals()))       #0.010286499999999997
print(timeit.timeit('my_func(my_array(1000))', number=100, globals=globals()))      #0.10295080000000001
print(timeit.timeit('my_func(my_array(10000))', number=100, globals=globals()))     #1.0472152000000001
#print(timeit.timeit('my_func(my_array(100000))', number=100, globals=globals()))    #10.2709747
#print(timeit.timeit('my_func(my_array(1000000))', number=100, globals=globals()))    #109.40559999999999

cProfile.run('my_func(my_array(100000))')

# 604810 function calls in 0.209 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.193    0.193 <string>:1(<module>)
#   100000    0.036    0.000    0.051    0.000 random.py:237(_randbelow_with_getrandbits)
#   100000    0.050    0.000    0.101    0.000 random.py:290(randrange)
#   100000    0.026    0.000    0.127    0.000 random.py:334(randint)
#        1    0.000    0.000    0.154    0.154 task_4_1.py:11(my_array)
#        1    0.028    0.028    0.154    0.154 task_4_1.py:14(<listcomp>)
#        1    0.032    0.032    0.038    0.038 task_4_1.py:18(my_func)
#        1    0.000    0.000    0.193    0.193 {built-in method builtins.exec}
#   100001    0.006    0.000    0.006    0.000 {built-in method builtins.len}
#   100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   104845    0.009    0.000    0.009    0.000 {method 'getrandbits' of '_random.Random' objects}


def my_func_1(num_list):
    max_el = min(num_list)
    for i, item in enumerate(num_list):
        if max_el < item < 0:
            max_el = item
            max_idx = i
    return f'В массиве: \n{num_list} \nминимальный отрицательный элемент = {max_el} \nего индекс = {max_idx}'


print(timeit.timeit('my_func_1(my_array(10))', number=100, globals=globals()))      #0.0011691999999996483
print(timeit.timeit('my_func_1(my_array(100))', number=100, globals=globals()))     #0.00966170000000055
print(timeit.timeit('my_func_1(my_array(1000))', number=100, globals=globals()))    #0.09063760000000087
print(timeit.timeit('my_func_1(my_array(10000))', number=100, globals=globals()))   #0.9601045999999993
#print(timeit.timeit('my_func_1(my_array(100000))', number=100, globals=globals()))  #8.866492699999998
#print(timeit.timeit('my_func_1(my_array(1000000))', number=100, globals=globals()))  #96.56381060000001

cProfile.run('my_func_1(my_array(100000))')

# 504786 function calls in 0.172 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.175    0.175 <string>:1(<module>)
#   100000    0.037    0.000    0.053    0.000 random.py:237(_randbelow_with_getrandbits)
#   100000    0.052    0.000    0.104    0.000 random.py:290(randrange)
#   100000    0.026    0.000    0.131    0.000 random.py:334(randint)
#        1    0.000    0.000    0.159    0.159 task_4_1.py:11(my_array)
#        1    0.029    0.029    0.159    0.159 task_4_1.py:14(<listcomp>)
#        1    0.013    0.013    0.014    0.014 task_4_1.py:39(my_func_1)
#        1    0.000    0.000    0.175    0.175 {built-in method builtins.exec}
#        1    0.001    0.001    0.001    0.001 {built-in method builtins.min}
#   100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   104765    0.009    0.000    0.009    0.000 {method 'getrandbits' of '_random.Random' objects}


def my_func_2(num_list):
    new_list = [i for i in num_list if i < 0]
    max_el = max(new_list)
    max_idx = num_list.index(max_el)
    return f'В массиве: \n{num_list} \nминимальный отрицательный элемент = {max_el} \nего индекс = {max_idx}'


print(timeit.timeit('my_func_2(my_array(10))', number=100, globals=globals()))      #0.0011191000000003726
print(timeit.timeit('my_func_2(my_array(100))', number=100, globals=globals()))     #0.008353099999997227
print(timeit.timeit('my_func_2(my_array(1000))', number=100, globals=globals()))    #0.08686240000000112
print(timeit.timeit('my_func_2(my_array(10000))', number=100, globals=globals()))   #0.8545726000000009
#print(timeit.timeit('my_func_2(my_array(100000))', number=100, globals=globals()))  #8.4346578
#print(timeit.timeit('my_func_2(my_array(1000000))', number=100, globals=globals())) #93.96939259999999

cProfile.run('my_func_2(my_array(100000))')

#  504861 function calls in 0.171 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.168    0.168 <string>:1(<module>)
#   100000    0.036    0.000    0.052    0.000 random.py:237(_randbelow_with_getrandbits)
#   100000    0.049    0.000    0.101    0.000 random.py:290(randrange)
#   100000    0.026    0.000    0.128    0.000 random.py:334(randint)
#        1    0.000    0.000    0.155    0.155 task_4_1.py:11(my_array)
#        1    0.027    0.027    0.155    0.155 task_4_1.py:14(<listcomp>)
#        1    0.008    0.008    0.012    0.012 task_4_1.py:57(my_func_2)
#        1    0.003    0.003    0.003    0.003 task_4_1.py:58(<listcomp>)
#        1    0.000    0.000    0.168    0.168 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#   100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   104987    0.009    0.000    0.009    0.000 {method 'getrandbits' of '_random.Random' objects}
#        1    0.001    0.001    0.001    0.001 {method 'index' of 'list' objects}
