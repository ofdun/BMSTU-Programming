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
    
for m in matrix:
    for elem in m:
        print(f"{elem:^5}", end=' ')
    print()
    
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
print('Итоговая матрица: ')
for m in matrix:
    for elem in m:
        print(f"{elem:^5}", end=' ')
    print()