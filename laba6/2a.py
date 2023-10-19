# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# 2a. Удалить элемент с заданным индексом с использованием
# любых средств Python.

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

for i in range(n):
    while True:
        elem = float(input(f"Введите {i + 1} элемент массива: "))
        if int(elem) != elem:
            print("Значение должно быть цесочисленным")
        else:
            elem = int(elem)
            arr.append(elem)
            break
    
while True:   
    index = float(input("Введите индекс, где нужно удалить элемент: "))
    if int(index) != index:
        print("Индекс должен быть целым")
    elif not(0 <= index < n):
        print("Индекс должен быть больше нуля, но меньше длины списка")
    else:
        index = int(index)
        break
    
arr.pop(index)

for c in arr:
    print(c, end=' ')