# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 5
# Назначение программы: 
# Найти строку, имеющую наибольшее количество нулевых элементов.

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
        
max_row = 0
max_number = 0
for i in range(n_rows):
    k = 0
    for j in range(n_columns):
        if matrix[i][j] == 0:
            k += 1
    if k > max_number:
        max_number = k
        max_row = i


print(f"Строка с наибольшим количеством нулей: {matrix[max_row]}")