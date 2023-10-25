# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# 1a. Добавить элемент в заданное место списка (по индексу) с использованием
# любых средств Python.

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
       
# Ввод элемента 
while True:
    elem = float(input(f"Введите элемент, который нужно добавить: "))
    if int(elem) != elem:
        print("Значение должно быть цесочисленным")
    else:
        elem = int(elem)
        break
    
# Ввод индекса
while True:   
    index = float(input("Введите индекс, куда нужно установить элемент: "))
    if int(index) != index:
        print("Индекс должен быть целым")
    elif not(0 <= index <= n):
        print("Индекс должен быть больше нуля, но не больше длины списка")
    else:
        index = int(index)
        break
    
# Добавляем элемент по индексу
arr.insert(index, elem)

# Вывод списка
print("Итоговый список: ", end='')
for c in arr:
    print(c, end=' ')
print()