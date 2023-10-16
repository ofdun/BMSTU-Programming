# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 5
# Назначение программы:
# 5. Поменять местами минимальный нечетный и максимальный четный элементы.

n = int(input('Введите длину списка: '))
arr = [int(input(f"Введите {i + 1} элемент массива: ")) for i in range(n)]
    
min_odd, max_even = float("+inf"), float("-inf")
min_odd_index, max_even_index = None, None
    
for i in range(n):
    if arr[i]%2 == 0:
        if arr[i] < min_odd:
            min_odd = arr[i]
            min_odd_index = i
    else:
        if arr[i] > max_even:
            max_even = arr[i]
            max_even_index = i
            
arr[min_odd_index], arr[max_even_index] = max_even, min_odd
    
print(arr)