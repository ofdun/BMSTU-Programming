# Вариант 5

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


k = 0
for i in range(n):
    if arr[i] >= 0:
        arr[k] = arr[i]
        k += 1        
n = k

for i in range(n):
    print(arr[i], end=' ')
print()