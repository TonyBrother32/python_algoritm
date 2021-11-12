import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_el = array[0]
min_el = array[1]

for i in array:
    if i > max_el:
        max_el = i
    elif i < min_el:
        min_el = i
array[array.index(min_el)], array[array.index(max_el)] = array[array.index(max_el)], array[array.index(min_el)]
print(f'Массив после изменения элементов {array.index(min_el)} и {array.index(max_el)}: {array}')
