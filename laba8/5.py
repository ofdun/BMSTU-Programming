# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 5
# Назначение программы: 
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю

# Ввод кол-ва столбцов и строк
while True:
    n = float(input('Введите количество строк и столбцов: '))
    if 0 < n <= int(n):
        n = int(n)
        break
    print("Количество строк должно быть натуральным")
    
matrix = [[0] * n for _ in range(n) ]

# Ввод матрицы
print("-" * 30)
for row in range(n):
    for column in range(n):
        matrix[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки: "))
    print("-" * 30)
    
if n == 1:
    max_above = "не существует"
    min_above = 'не существует'
else:
    max_above = matrix[0][1]
    min_above = matrix[1][n-1]
    
for i in range(n):
    # Перебор над главной диаганалью
    for j in range(i + 1, n):
        if matrix[i][j] > max_above:
            max_above = matrix[i][j]
    
    # Перебор под побочной диагональю
    for j in range(n - i, n):
        if matrix[i][j] < min_above:
            min_above = matrix[i][j]
            
print(f"Максимальное число над главной диагональю - {max_above}")
print(f"Минимальное число под побочной диагональю - {min_above}")