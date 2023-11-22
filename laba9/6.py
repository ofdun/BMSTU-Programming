# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V

# Ввод матрицы A
while True:
    n = float(input('Введите количество строк матриц: '))
    if 0 < n <= int(n):
        n = int(n)
        break
    print("Количество строк должно быть натуральным")
    
while True:
    columns = float(input('Введите количество столбцов матриц: '))
    if 0 < columns <= int(columns):
        columns = int(columns)
        break
    print("Количество столбцов должно быть натуральным")
    
A = [[0] * columns for _ in range(n) ]

print("-" * 30)
for row in range(n):
    for column in range(columns):
        A[row][column] = float(input(f"Введите {row + 1} элемент {column + 1} строки матрицы A: "))
    print("-" * 30)

B = [[0] * columns for _ in range(n) ]

for row in range(n):
    for column in range(columns):
        B[row][column] = float(input(f"Введите {row + 1} элемент {column + 1} строки матрицы B: "))
    print("-" * 30)

C = [[0] * columns for _ in range(n) ]

# Заполним C
for i in range(n):
    for j in range(columns):
        C[i][j] = A[i][j] * B[i][j]

V = [0] * columns

for j in range(columns):
    for i in range(n):
        V[j] += C[i][j]

print("Матрица A: ")
print("-"*(columns*12 + (columns + 1)))
for i in range(n):
    print("|", end='')
    for j in range(columns):
        print(f"{A[i][j]:^12.5g}|", end='')
    print()
print("-"*(columns*12 + (columns + 1)))

print("Матрица B: ")
print("-"*(columns*12 + (columns + 1)))
for i in range(n):
    print("|", end='')
    for j in range(columns):
        print(f"{B[i][j]:^12.5g}|", end='')
    print()
print("-"*(columns*12 + (columns + 1)))

print("Матрица C: ")
print("-"*(columns*12 + (columns + 1)))
for i in range(n):
    print("|", end='')
    for j in range(columns):
        print(f"{C[i][j]:^12.5g}|", end='')
    print()
print("-"*(columns*12 + (columns + 1)))

print(f"Массив V: {V}")
