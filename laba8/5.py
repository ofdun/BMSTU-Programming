# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 5
# Назначение программы: 
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю


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
    
max_above = float('-inf')
min_above = float("+inf")
    
# Перебор над главной диаганалью
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] > max_above:
            max_above = matrix[i][j]
    
    for j in range(0, i):
        if matrix[i][j] < min_above:
            min_above = matrix[i][j]
            
print(f"Максимальное число над главной диагональю равно {max_above}")
print(f"Максимальное число под побочной диагональю равно {min_above}")