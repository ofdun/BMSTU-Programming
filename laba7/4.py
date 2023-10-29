# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 3
# Назначение программы: 
# Замена всех заглавных согласных английских букв на строчные

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
    
for i in range(n):
    string = ''
    for char in arr[i]:
        # Если заглавная и не гласная  
        if char.isupper() and char not in "AEIOUY":
            string += char.lower()
        else:
            string += char
    arr[i] = string

print("Итоговый список: ", end='')

for i in range(n):
    print(arr[i], end=' ')
print()
