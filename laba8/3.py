while True:
    n_rows = float(input('Введите количество строк: '))
    if 0 < n_rows <= int(n_rows):
        n_rows = int(n_rows)
        break
    print("Количество строк должно быть натуральным")
    
while True:
    n_columns = float(input('Введите количество столбцов: '))
    if 0 < n_columns <= int(n_columns):
        n_columns = int(n_columns)
        break
    print("Количество столбцов должно быть натуральным")
    
matrix = [[0] * n_columns for _ in range(n_rows) ]

print("-" * 30)
for row in range(n_rows):
    for column in range(n_columns):
        matrix[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки: "))
    print("-" * 30)
        
max_column = 0
max_number = 0
for j in range(n_columns):
    k = 0
    for i in range(n_rows):
        print(matrix[i][j], end=' ')
        if matrix[i][j] % 2 == 0 or matrix[i][j] == 1:
            k += 1
    if k > max_number:
        max_number = k
        max_column = j
    print()
print("Cтолбец с наибольшим количеством чисел, являющимися степенью 2: ", end='')
for i in range(n_rows):
    print(matrix[i][max_column], end=' ')