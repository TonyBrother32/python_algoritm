import random

SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


num = array[0]
max_frq = 1
for i in range(SIZE-1):
    frq = 1
    for k in range(i+1,SIZE):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print('Все числа массива встречаются один раз')
