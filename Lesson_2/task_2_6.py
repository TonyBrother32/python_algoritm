import random

digit = random.randint(0, 101)
i = 1
while i <= 10:
    print(f'Попытка №{i:2} из 10')
    user_n = int(input('Введите число от 1 до 100: '))
    if user_n == digit:
        print('Вы угадали загаданное число')
        break
    elif user_n > digit:
        print(f'Число {user_n} больше загаданного')
    else:
        print(f'Число {user_n} меньше загаданного')
    i += 1
if i > 10:
    print(f'Не угадали! Загаданное число {digit}')
