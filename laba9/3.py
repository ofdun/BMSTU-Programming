# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G

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
        D[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки матрицы D: "))
    print("-" * 30)

# Ввод матрицы Z
while True:
    n_rows_Z = float(input('Введите количество строк матрицы Z: '))
    if 0 < n_rows_Z <= int(n_rows_Z):
        if n_rows_Z >= n_rows_D:
            n_rows_Z = int(n_rows_Z)
            break
        else:
            print("Строк в Z не может быть меньше чем в D")
    else:
        print("Количество строк должно быть натуральным")
    
while True:
    n_columns_Z = float(input('Введите количество столбцов матрицы Z: '))
    if 0 < n_columns_Z <= int(n_columns_Z):
        n_columns_Z = int(n_columns_Z)
        break
    print("Количество столбцов должно быть натуральным")
    
Z = [[0] * n_columns_Z for _ in range(n_rows_Z) ]

print("-" * 30)
for row in range(n_rows_Z):
    for column in range(n_columns_Z):
        Z[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки матрицы Z: "))
    print("-" * 30)

# Вывод матрицы Z
print("Исходная матрица Z: ")
print("-"*(n_columns_Z*12 + (n_columns_Z + 1)))
for i in range(n_rows_Z):
    print("|", end='')
    for j in range(n_columns_Z):
        print(f"{Z[i][j]:^12.5g}|", end='')
    print()
print("-"*(n_columns_Z*12 + (n_columns_Z + 1)))

# Вывод матрицы D
print("Исходная матрица D: ")
print("-"*(n_columns_D*12 + (n_columns_D + 1)))
for i in range(n_rows_D):
    print("|", end='')
    for j in range(n_columns_D):
        print(f"{D[i][j]:^12.5g}|", end='')
    print()
print("-"*(n_columns_D*12 + (n_columns_D + 1)))

# Объявим массив G
G = [0] * n_rows_D

# Заполним массив G суммами строк матрицы Z
for i in range(n_rows_Z):
    sum_ = 0
    for j in range(n_columns_Z):
        sum_ += Z[i][j]
    G[i] = sum_

max_elem = 0

# Подсчитаем кол-во эл. в каждой строке D превосходящее сумму ряда в Z
# Также найдем максимум
for i in range(n_rows_D):
    counter = 0
    for j in range(n_columns_D):
        if D[i][j] > G[i]:
            counter += 1
    if counter > max_elem:
        max_elem = counter
    G[i] = counter


# Умножим матрицу D на max_elem
for i in range(n_rows_D):
    for j in range(n_columns_D):
        D[i][j] *= max_elem

# Вывод матрицы D
print("Итоговая матрица D: ")
print("-"*(n_columns_D*12 + (n_columns_D + 1)))
for i in range(n_rows_D):
    print("|", end='')
    for j in range(n_columns_D):
        print(f"{D[i][j]:^12.5g}|", end='')
    print()
print("-"*(n_columns_D*12 + (n_columns_D + 1)))

# Вывод массива G
print(f"Массив G: {G}")