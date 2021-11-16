# В алгоритме с решетом Эратосфена почему то получилась линейная зависимость,
# которая больше зависела от длинны массива, а не от порядкового номера числа в нем.
# Алгоритм без решета Эратосфена был быстрее только при длинне массива менее 100 чисел. Далее время выполенения
# увеличивалось скорее всего на log(n)

import cProfile
import timeit


def sieve(num, idx):
    array = [i for i in range(num)]
    array[1] = 0
    for i in range(2, num):
        if array[i] != 0:
            j = i + i
            while j < num:
                array[j] = 0
                j += i
    res = [i for i in array if i != 0]
    return f' {idx} по порядку простое число равно {res[idx-1]}'


print(timeit.timeit('sieve(99,9)', number=100, globals=globals()))         #0.001776799999999995
print(timeit.timeit('sieve(990,90)', number=100, globals=globals()))       #0.021937000000000005
print(timeit.timeit('sieve(9900,900)', number=100, globals=globals()))     #0.2291107
print(timeit.timeit('sieve(99000,9000)', number=100, globals=globals()))   #2.5468778

cProfile.run('sieve(99999,999)')

#6 function calls in 0.027 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.027    0.027 <string>:1(<module>)
#        1    0.002    0.002    0.002    0.002 task_4_2.py:14(<listcomp>)
#        1    0.021    0.021    0.026    0.026 task_4_2.py:5(sieve)
#        1    0.003    0.003    0.003    0.003 task_4_2.py:6(<listcomp>)
#        1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def prime(num, idx):
    array = [i for i in range(num)]
    array[1] = 0
    s_nums = []
    for i in range(2, num):
        for n in s_nums:
            if array[i] % n == 0:
                break
        else:
            s_nums.append(array[i])
        if len(s_nums) == idx:
            return f' {idx} по порядку простое число равно {s_nums[-1]}'


print(timeit.timeit('prime(99,9)', number=100, globals=globals()))         #0.0009753999999997376
print(timeit.timeit('prime(999,90)', number=100, globals=globals()))       #0.03090409999999988
print(timeit.timeit('prime(9999,900)', number=100, globals=globals()))     #2.3602838
#print(timeit.timeit('prime(99999,9000)', number=100, globals=globals()))   #225.6821829


cProfile.run('prime(99999,999)')

#8910 function calls in 0.035 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.034    0.034 <string>:1(<module>)
#        1    0.030    0.030    0.034    0.034 task_4_2.py:26(simple_num)
#        1    0.003    0.003    0.003    0.003 task_4_2.py:27(<listcomp>)
#        1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
#     7906    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}