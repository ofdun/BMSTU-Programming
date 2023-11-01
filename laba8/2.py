# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 5
# Назначение программы: 
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов.

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
        
count_max_neg = float('+inf')
count_min_neg = float('-inf')
count_max_neg_index = 0
count_min_neg_index = 0

for i in range(n_rows):
    count_neg = 0
    for j in range(n_columns):
        if matrix[i][j] < 0:
            count_neg += 1
            
    if count_min_neg < count_neg:
        count_min_neg = count_neg
        count_min_neg_index = i
        
    if count_max_neg > count_neg:
        count_max_neg_index = i
        count_max_neg = count_neg

matrix[count_max_neg_index], matrix[count_min_neg_index] = \
    matrix[count_min_neg_index], matrix[count_max_neg_index]        

print('Итоговая матрица: ')
for m in matrix:
    for elem in m:
        print(f"{elem:^5}", end=' ')
    print()