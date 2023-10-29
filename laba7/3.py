# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 4
# Назначение программы: 
# Поиск элемента в списке строк с максимальным количеством пробелов подряд

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
    elem = input(f"Введите {i + 1} элемент массива: ")
    arr.append(elem)

n = len(arr)

# Заводим переменные для храния максимума и его индекса
count_max = 0
count_max_index = 0

for i in range(n):
    k = 0
    for c in arr[i]:
        if c == ' ':
            k += 1
            if k > count_max:
                count_max = k
                count_max_index = i
        else:
            k = 0

answer = arr[count_max_index]

print(f'Элемент с наибольшим количеством пробелов, идущих подряд: "{answer}"')