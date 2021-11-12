import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
result = []
for i in array:
    if i % 2 == 0:
        result.append(array.index(i))

print(f'Для массива: {array} индексы четных элементов: {result}')
### Если попадается два одинаковых четных числа в сгенерерированном масиве почему то во второй массив идет только индекс первого несколько раз
