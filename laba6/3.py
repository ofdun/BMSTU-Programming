# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# 3. Найти значение K-го экстремума в списке.

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
    k = float(input("Введите K-ый экстремум, который надо найти: "))
    if int(k) != k:
        print("K-ый экстремум должен быть целым")
    elif not(0 <= k < n):
        print("K-ый экстремум должен быть больше нуля, но меньше длины списка")
    else:
        k = int(k)
        break
answer = ""

for i in range(1, n - 1):
    if not k:
        answer = arr[i - 1]
        break
    elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        k -= 1
    elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
        k -= 1
        
if k == 0 and not answer:
    answer = arr[-2]
elif not answer:
    answer = "Такого экстремума нет в списке"

print(answer)