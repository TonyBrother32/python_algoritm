import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
index = -1
while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif array[index] < array[i] < 0:
        index = i
    i += 1
print(f'Индекс элемента {index}, Значение элемента {array[index]}')
