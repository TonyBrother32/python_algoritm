# 5 задание к 3 уроку
# В массиве найти максимальный отрицательный элемент и вывести на экран его значение и позицию в массиве.
# Версия python 3.9.1, Win10 64.
# При 100 элементах затраты памяти первым вариантом = 1004, вторым = 1096, третьим = 1448
# При 1000 элементах затраты памяти первым вариантом = 8940, вторым = 9032, третьим = 13128
# При 10000 элементах затраты памяти первым вариантом = 85260, вторым = 85352, третьим = 127112
# С ростом числа элементов третий вариант забирает памяти больше остальных, я так понимаю растет количество ссылок на значения
# Разница между первым и вторым вариантом минимальна. Учитывая что второй вариант оптимальнее по затратам времени -
# он и лучше остальных в итоге
#

import random
from sys import getsizeof


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
    return f'В массиве минимальный отрицательный элемент = {num_list[index]} его индекс = {index} \nиспользуемая ' \
           f'память = {getsizeof(num_list) + getsizeof(i) + getsizeof(index) + getsizeof(len(num_list))}'


def my_func_1(num_list):
    max_el = min(num_list)
    for i, item in enumerate(num_list):
        if max_el < item < 0:
            max_el = item
            max_idx = i
    return f'В массиве минимальный отрицательный элемент = {max_el} его индекс = {max_idx} \nиспользуемая память = ' \
           f'{getsizeof(num_list) + getsizeof(max_el) + getsizeof(i) + getsizeof(item) + getsizeof(max_idx) + getsizeof(enumerate(num_list))}'


def my_func_2(num_list):
    new_list = [i for i in num_list if i < 0]
    max_el = max(new_list)
    max_idx = num_list.index(max_el)
    return f'В массиве мининимальный отрицательный элемент = {max_el} его индекс = {max_idx} \nиспользуемая ' \
           f'память = {getsizeof(num_list) + getsizeof(new_list) + getsizeof(max_el) + getsizeof(max_idx)}'


# print(my_func(my_array(100)))
# print(my_func(my_array(1000)))
# print(my_func(my_array(10000)))

# print(my_func_1(my_array(100)))
# print(my_func_1(my_array(1000)))
# print(my_func_1(my_array(10000)))

# print(my_func_2(my_array(100)))
# print(my_func_2(my_array(1000)))
# print(my_func_2(my_array(10000)))
