# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# Даны массивы D и F. Сформировать матрицу A по формуле
# ajk = sin(dj+fk)
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.

from math import sin

# Ввод массивов
# Ввод длины массива D
while True:
    lenD = float(input('Введите длину массива D: '))
    if lenD < 0:
        print("Длина массива должна быть больше 0")
    elif int(lenD) != lenD:
        print("Длина массива должна быть целочисленной")
    else:
        lenD = int(lenD)
        break

D = []

# Ввод массива D
for i in range(lenD):
    while True:
        elem = float(input(f"Введите {i + 1} элемент массива D: "))
        D.append(elem)
        break

# Ввод длины массива F
while True:
    lenF = float(input('Введите длину массива F: '))
    if lenF < 0:
        print("Длина массива должна быть больше 0")
    elif int(lenF) != lenF:
        print("Длина массива должна быть целочисленной")
    else:
        lenF = int(lenF)
        break

F = []

# Ввод массива F
for i in range(lenF):
    while True:
        elem = float(input(f"Введите {i + 1} элемент массива F: "))
        elem = int(elem)
        F.append(elem)
        break

A = [[0]*lenF for _ in range(lenD)]

# Массив средних арифметических больше нуля
AV = [0] * lenD
# Массив чисел, меньших среднего арифметического
L = [0] * lenD

# Заполняем матрицу А и сразу же считаем среднее арифм. пол. чисел
for j in range(lenD):
    counter = 0
    sum_ = 0
    for k in range(lenF):
        A[j][k] = sin(D[j] + F[k])
        if A[j][k] > 0:
            sum_ += A[j][k]
            counter += 1
    if counter != 0:
        avg_ariphm = sum_ / counter
    else:
        avg_ariphm = "∅"
    # Добавляем ср. арифм. в массив
    AV[j] = avg_ariphm

# Считаем числа меньше среднего арифм. строки
for j in range(lenD):
    counter = 0

    if AV[j] == '∅':
        counter = '∅'
    else:
        for k in range(lenF):
            if A[j][k] < AV[j]:
                counter += 1

    L[j] = counter

# Выводим матрицу и массивы AV и L
print("-"*(lenF*12 + (lenF + 1)) + f"{'Ср.Арифм':^12}" + f"{'Меньше Ср.Арифм.'}")
for j in range(lenD):
    print("|", end='')
    for k in range(lenF):
        print(f"{A[j][k]:^12.5g}|", end='')

    # Если существует ср. арифм. то брать 5 знач. цифр
    if AV[j] != '∅':
        print(f"{AV[j]:^12.5g}|", end='')
    else:
        print(f"{AV[j]:^12}|", end='')
    
    # Если существует кол-во чисел меньше ср арифм, то брать 5 знач. цифр
    if L[j] != '∅':
        print(f"{L[j]:^13.5g}|", end='')
    else:
        print(f"{L[j]:^13}|", end='')

    print()
print("-"*(lenF*12 + (lenF + 1)))