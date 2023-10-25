# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# 2b. Удалить элемент с заданным индексом алгоритмически.

# Ввод длины списка
while True:
    n = float(input('Введите длину списка: '))
    if n < 0:
        print("Длина списка должна быть больше 0")
    elif int(n) != n:
        print("Длина списка должна быть целочисленной")
    else:
        n = int(n)
        break

arr = []

# Ввод списка
for i in range(n):
    while True:
        elem = float(input(f"Введите {i + 1} элемент массива: "))
        if int(elem) != elem:
            print("Значение должно быть цесочисленным")
        else:
            elem = int(elem)
            arr.append(elem)
            break

# Ввод индекса
while True:   
    index = float(input("Введите индекс, где нужно удалить элемент: "))
    if int(index) != index:
        print("Индекс должен быть целым")
    elif not(0 <= index < n):
        print("Индекс должен быть больше нуля, но меньше длины списка")
    else:
        index = int(index)
        break

# Удаляем элемент по индексу
for i in range(index + 1, n):
    arr[i - 1] = arr[i]
arr.pop()

# Вывод списка
print("Итоговый список: ", end='')
for c in arr:
    print(c, end=' ')
print()