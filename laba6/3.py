# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: 
# 3. Найти значение K-го экстремума в списке.

n = int(input('Введите длину списка: '))
arr = [int(input(f"Введите {i + 1} элемент массива: ")) for i in range(n)]
k = int(input("Введите K-ый экстремум, который надо найти: "))
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
    answer = "Такого элемента нет в списке"

print(answer)