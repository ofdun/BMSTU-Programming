# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 9
# Назначение программы: 
# 4. Найти наиболее длинную непрерывную Убывающая последовательность
# отрицательных чисел, модуль которых является простым числом.

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
            print("Значение должно быть целочисленным")
        else:
            elem = int(elem)
            arr.append(elem)
            break
k = 0

prime = False
# Проверяем первый элемент списка на простое число
num = arr[0]
if num < 0:
    prime = True
    num = -num
    prime = num != 1
    d = 2
    while d**2 < num and prime:
        if num % d == 0:
            prime = False
        else:
            d += 1
            
# k = 1 если первое число удовл. условиям, иначе k=0
k = int(prime is True)
max_posl = k
for i in range(1, n):
    if arr[i] < arr[i - 1] and arr[i] < 0 and arr[i - 1] < 0:
        num = -arr[i]
        # Алгоритм проверки на простое число
        prime = num != 1
        d = 2
        while d**2 <= num and prime:
            if num % d == 0:
                prime = False
            else:
                d += 1
        if prime:
            if k == 0:
                k = 2
            else:
                k += 1
            if max_posl < k:
                max_posl = k
                max_index = i
        else:
            k = 0
    else:
        k = 0

# Вывод
print("Наибольшая убывающая последовательность отрицательных чисел:", end=' ')
for i in range(max_index - max_posl + 1, max_index + 1):
    print(arr[i], end=' ')
print()
