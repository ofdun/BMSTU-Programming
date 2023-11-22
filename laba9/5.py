# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

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
        while True:
            elem = input(f"Введите {row + 1} элемент {column + 1} строки матрицы D: ")
            if len(elem) == 1:
                D[row][column] = elem
                break
            print("Введите один символ!")
    print("-" * 30)

print("Исходная матрица D: ")
print("-"*(n_columns_D*12 + (n_columns_D + 1)))
for i in range(n_rows_D):
    print("|", end='')
    for j in range(n_columns_D):
        print(f"{D[i][j]:^12}|", end='')
    print()
print("-"*(n_columns_D*12 + (n_columns_D + 1)))

for i in range(n_rows_D):
    for j in range(n_columns_D):
        if D[i][j] in "aoieuyAOIEUY":
            D[i][j] = '.'
    

print("Итоговая матрица D: ")
print("-"*(n_columns_D*12 + (n_columns_D + 1)))
for i in range(n_rows_D):
    print("|", end='')
    for j in range(n_columns_D):
        print(f"{D[i][j]:^12}|", end='')
    print()
print("-"*(n_columns_D*12 + (n_columns_D + 1)))