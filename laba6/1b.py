# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# 1b. Добавить элемент в заданное место списка (по индексу) алгоритмически.

n = int(input('Введите длину списка: '))
arr = [int(input(f"Введите {i + 1} элемент массива: ")) for i in range(n)]
element = int(input(f"Введите элемент, который нужно добавить: "))
index = int(input("Введите индекс, куда нужно установить элемент: "))
arr.append(None)
for i in range(n, -1, -1):
    if i != index:
        arr[i] = arr[i - 1]
    else:
        arr[i] = element
        break
    
print(arr)