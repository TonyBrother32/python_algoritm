import random


def median(array, k):
    if len(array) == 1:
        return array[0]

    spam = random.choice(array)
    left_el = [el for el in array if el < spam]
    right_el = [el for el in array if el > spam]
    spam = [el for el in array if el == spam]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(spam):
        return spam[0]
    else:
        return median(right_el, k - len(left_el) - len(spam))


M = 7
lst = [random.randint(0, 50) for _ in range(2 * M + 1)]
print(f'Исходный массив:\n{lst}')
print(f'Медианой является:\n{median(lst, len(lst) / 2)}')
lst.sort()
print(f'Массив после сортировки:\n{lst}')
print(f'Медианой является:\n{lst[len(lst) // 2]}')