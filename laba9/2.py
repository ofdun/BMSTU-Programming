# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки.

# Ввод матрицы
while True:
    n = float(input('Введите количество строк и столбцов: '))
    if 0 < n <= int(n):
        n = int(n)
        break
    print("Количество строк должно быть натуральным")
    
matrix = [[0] * n for _ in range(n) ]

print("-" * 30)
for row in range(n):
    for column in range(n):
        matrix[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки: "))
    print("-" * 30)

print("Исходная матрица: ")
# Выводим матрицу
print("-"*(n*12 + (n + 1)))
for i in range(n):
    print("|", end='')
    for j in range(n):
        print(f"{matrix[i][j]:^12.5g}|", end='')
    print()
print("-"*(n*12 + (n + 1)))

# Повернем матрицу на 90 градусов вправо.
for i in range(n // 2):
    for j in range(i, n - i - 1):
        # Запомним первый элемент перед поворотом
        tmp = matrix[i][j]
        matrix[i][j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
        matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        matrix[j][n - 1 - i] = tmp
        
print("Промежуточная матрица: ")
print("-"*(n*12 + (n + 1)))
for i in range(n):
    print("|", end='')
    for j in range(n):
        print(f"{matrix[i][j]:^12.5g}|", end='')
    print()
print("-"*(n*12 + (n + 1)))


for i in range(n // 2):
    for j in range(i, n - 1 - i):
        # Запомним первый элемент перед поворотом
        tmp = matrix[i][j]
        matrix[i][j] = matrix[j][n - 1 - i]
        matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
        matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = tmp

print("Итоговая матрица: ")
print("-"*(n*12 + (n + 1)))
for i in range(n):
    print("|", end='')
    for j in range(n):
        print(f"{matrix[i][j]:^12.5g}|", end='')
    print()
print("-"*(n*12 + (n + 1)))