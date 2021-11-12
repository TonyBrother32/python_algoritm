count = dict.fromkeys(range(2, 10), 0)
for num in range(2, 100):
    for i in range(2, 10):
        if num % i == 0:
            count[i] += 1
for key in count:
    print(f'{key} кратны {count[key]} чисел')
