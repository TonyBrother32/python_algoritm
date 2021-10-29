x1 = float(input('Введите кординаты x1 '))
y1 = float(input('Введите кординаты y1 '))
x2 = float(input('Введите кординаты x2 '))
y2 = float(input('Введите кординаты y2 '))
k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1
print(f'Уравнение прямой: y = {k}x + {b}')
