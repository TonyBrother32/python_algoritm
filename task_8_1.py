def count(string):
    count_list = []
    for i in range(1, len(string)):
        j = 0
        for j in range(len(string) - j):
            sub_str = hash(string[j:j + i])
            if sub_str not in count_list:
                count_list.append(sub_str)
    return f'Количество разных подстрок в строке {string} равно {len(count_list)}'


print(count('papa'))
