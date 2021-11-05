n = range(32, 128)
for i in n:
    if i % 10 == 0:
        print(f'{i} {chr(i):3}')
    else:
        print(f'{i} {chr(i):3}', end=' ')
