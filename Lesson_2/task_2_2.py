digit = input('Введите целое число: ')
even = 0
odd = 0
for i in digit:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'В числе {digit} {even} четных цифры и {odd} нечетных')
