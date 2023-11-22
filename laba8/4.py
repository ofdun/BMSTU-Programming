# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 5
# Назначение программы: 
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов.

# Ввод кол-ва строк
while True:
    n_rows = float(input('Введите количество строк: '))
    if 0 < n_rows <= int(n_rows):
        n_rows = int(n_rows)
        break
    print("Количество строк должно быть натуральным")

# Ввод кол-ва столбцов  
while True:
    n_columns = float(input('Введите количество столбцов: '))
    if 0 < n_columns <= int(n_columns):
        n_columns = int(n_columns)
        break
    print("Количество столбцов должно быть натуральным")
    
matrix = [[0] * n_columns for _ in range(n_rows) ]

# Ввод матрицы поэлементно
print("-" * 30)
for row in range(n_rows):
    for column in range(n_columns):
        matrix[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки: "))
    print("-" * 30)
    
max_column = min_column = 0
max_number_column = min_number_column = 0

# Определяем столбцы с макс. и мин. суммой элементов
for j in range(n_columns):
    sum_ = 0
    for i in range(n_rows):
        sum_ += matrix[i][j]
            
    # Обновляем минимум
    if min_number_column < sum_:
        min_number_column = sum_
        min_column = j
        
    # Обновляем максимум
    if max_number_column > sum_:
        max_number_column = sum_
        max_column = j
    
# Меняем столбцы местами 
for i in range(n_rows):
    matrix[i][min_column], matrix[i][max_column] = \
        matrix[i][max_column], matrix[i][min_column]
        
# Вывод матрицы
print('Итоговая матрица: ')
for m in matrix:
    for elem in m:
        print(f"{elem:^5}", end=' ')
    print()