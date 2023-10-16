# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 10
# Назначение программы: 
# 4. Найти наиболее длинную непрерывную Убывающая последовательность
# отрицательных чисел, модуль которых является простым числом.

n = int(input('Введите длину списка: '))
arr = [int(input(f"Введите {i + 1} элемент массива: ")) for i in range(n)]
k = 0

# Проверяем первый элемент списка на простое число
num = arr[0]
if num < 0:
    num = -num
    prime = num != 1
    d = 2
    while d**2 < num and prime:
        if num % d == 0:
            prime = False
        else:
            d += 1

k = 1 if prime else 0
max_ = k
for i in range(1, n):
    if arr[i] < arr[i - 1] and arr[i] < 0:
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
            k += 1
            if max_ < k:
                max_ = k
        else:
            k = 0
    else:
        k = 0

print(f"Длина наибольшей убывающей последовательности отр. чисел равна: {max_}")