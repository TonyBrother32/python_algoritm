a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if b < a < c or c < a < b:
    print(f'Среднее число: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')
