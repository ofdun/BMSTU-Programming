# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 5
# Назначение программы: 
# После каждого отрицательного элемента целочисленного списка,
# добавить его удвоенное значение

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
        
k = 0
for i in range(n):
    if arr[i] < 0:
        arr.append(None)
        k += 1
        
new_n = n + k
        
for i in range(n-1, -1, -1):
    if arr[i] >= 0:
        arr[i + k] = arr[i]
    else:
        arr[i + k] = arr[i] * 2
        arr[i + k - 1] = arr[i]
        k -= 1

print("Итоговый список: ", end='')
for i in range(new_n):
    print(arr[i], end=' ')
print()