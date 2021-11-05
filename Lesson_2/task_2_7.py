def left_side(n):
    if n == 1:
        return n
    return n + left_side(n-1)


def right_side(n):
    return n * (n + 1) // 2


n = 1
while n < 999:
    if left_side(n) == right_side(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')
        break
    n += 1
