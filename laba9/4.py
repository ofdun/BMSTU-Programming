# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.

# Ввод матрицы D
while True:
    n_rows_D = float(input('Введите количество строк матрицы D: '))
    if 0 < n_rows_D <= int(n_rows_D):
        n_rows_D = int(n_rows_D)
        break
    print("Количество строк должно быть натуральным")
    
while True:
    n_columns_D = float(input('Введите количество столбцов матрицы D: '))
    if 0 < n_columns_D <= int(n_columns_D):
        n_columns_D = int(n_columns_D)
        break
    print("Количество столбцов должно быть натуральным")
    
D = [[0] * n_columns_D for _ in range(n_rows_D) ]

print("-" * 30)
for row in range(n_rows_D):
    for column in range(n_columns_D):
        D[row][column] = float(input(f"Введите {row + 1} элемент {column + 1} строки матрицы D: "))
    print("-" * 30)

# Ввод массива I
# Ввод длины списка I
while True:
    n_I = float(input('Введите длину списка I: '))
    if n_I < 0:
        print("Длина списка должна быть больше 0")
    elif int(n_I) != n_I:
        print("Длина списка должна быть целочисленной")
    elif n_I > n_rows_D:
        print("Список не может быть больше, чем строк у матрицы D")
    else:
        n_I = int(n_I)
        break

I = []

# Ввод списка I
for i in range(n_I):
    while True:
        elem = float(input(f"Введите {i + 1} элемент массива I: "))
        if int(elem) != elem:
            print("Значение должно быть целочисленным")
        if elem > n_rows_D - 1:
            print("Строка должна присутствовать в D")
        else:
            elem = int(elem)
            I.append(elem)
            break

R = []

# Ищем макс. эл. в строках из массива I
sum_ = 0
for i in I:
    max_elem = D[i][0]
    for j in range(1, n_columns_D):
        if D[i][j] > max_elem:
            max_elem = D[i][j]
    sum_ += max_elem
    R.append(max_elem)

ariphm = sum_ / n_I


print("Матрица D: ")
print("-"*(n_columns_D*12 + (n_columns_D + 1)))
for i in range(n_rows_D):
    print("|", end='')
    for j in range(n_columns_D):
        print(f"{D[i][j]:^12.5g}|", end='')
    print()
print("-"*(n_columns_D*12 + (n_columns_D + 1)))

print(f"Массив I:", end=' ')
for elem in R: 
    print(f"{elem:.5g}", end=' ')
print()
print(f"Массив R:", end=' ')
for elem in R: 
    print(f"{elem:.5g}", end=' ')
print()
print(f"Среднее арифеметическое: {ariphm:.5g}")