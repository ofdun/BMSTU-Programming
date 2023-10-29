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
    
arr = [[0] * n_columns for _ in range(n_rows) ]

for row in range(n_rows):
    for column in range(n_columns):
        arr[row][column] = int(input(f"Введите {row + 1} элемент {column + 1} строки: "))
        
count_max_neg = 0
count_min_neg = 0
count_max_neg_index = 0
count_min_neg_index = 0

for row in range(n_rows):
    count_neg = 0
    for column in range(n_columns):
        if arr[row][column] < 0:
            count_neg += 1
            
    if count_min_neg > count_neg:
        count_min_neg = count_neg
        count_min_neg_index = row
        
    if count_max_neg < count_neg:
        count_max_neg_index = row
        count_max_neg = count_neg

arr[count_max_neg_index], arr[count_min_neg_index] = \
    arr[count_min_neg_index], arr[count_max_neg_index]        

for elem in arr:
    print(*elem)