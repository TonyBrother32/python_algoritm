input_range = input('Введите последовательность: ')
number = input('Введите цифру для поиска: ')
count = 0

for i in input_range:
    if i == number:
        count += 1

print(f'Цифра {number} встречается в последовательности #{input_range}# {count} раз(а)')
