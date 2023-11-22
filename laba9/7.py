# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1).

while True:
    x = int(input("Введите x матрицы: "))
    if x <= 0:
        print("x должен быть больше 0!")
    else:
        break

while True:
    y = int(input("Введите y матрицы: "))
    if y <= 0:
        print("y должен быть больше 0!")
    else:
        break

while True:
    z = int(input("Введите z матрицы: "))
    if z <= 0:
        print("z должен быть больше 0!")
    else:
        break

matrix = [[[0] * x for _ in range(y)] for _ in range(z)]

# Ввод
for i in range(z):
    for j in range(y):
        for k in range(x):
            elem = int(input(f'Введите элемент с z = {i + 1} и y = {j + 1} и x = {k + 1}: '))
            matrix[i][j][k] = elem

while True:
    index = int(input("Введите индекс среза: "))
    if 0 < index <= y:
        break
    print("Индекс должен быть от 0 до y")

for i in range(z):
    for k in range(x):
        print(f'Элемент с z = {i + 1} и y = {index} и x = {k + 1}: {matrix[i][index - 1][k]}')