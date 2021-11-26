import random


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        count = 0
        for i in range(len(arr) - 1 - (n - 1)):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
        if count == 0:
            break
        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')
