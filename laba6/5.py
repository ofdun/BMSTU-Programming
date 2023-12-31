# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 5
# Назначение программы:
# 5. Поменять местами минимальный четный и максимальный нечетный элементы.

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
    
min_even, max_odd = float("+inf"), float("-inf")
min_even_index, max_odd_index = None, None
    
for i in range(n):
    # Если есть меньше чем максимум (меньше чем минимум), обновляем
    if arr[i]%2 == 0:
        if arr[i] < min_even:
            min_even = arr[i]
            min_even_index = i
    else:
        if arr[i] > max_odd:
            max_odd = arr[i]
            max_odd_index = i
    
if max_odd_index is not None and min_even_index is not None:
    arr[min_even_index], arr[max_odd_index] = max_odd, min_even
    
print("Итоговый массив: ", end='')
for c in arr:
    print(c, end=' ')
print()
