year = int(input('Введите год: '))
if year % 400 == 0:
    print(f"Год {year} високосный")
elif year % 100 != 0 and year % 4 == 0:
    print(f"Год {year} високосный")
else:
    print(f"Год {year} невисокосный")
