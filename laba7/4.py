# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант: 3
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
# Разница между заглавными и строчными в юникоде
DIFF = 32

# Ввод списка
for i in range(n):
    elem = input(f"Введите {i + 1} элемент массива: ")
    arr.append(elem)
    
for i in range(n):
    string = ''
    for char in arr[i]:
        char_code = ord(char)
        # Если заглавная и не гласная  
        if 65 <= char_code <= 97 and char not in "AEIOUY":
            new_char = chr(char_code + DIFF)
            string += new_char
        else:
            string += char
    arr[i] = string

print("Итоговый список: ", end='')

for i in range(n):
    print(arr[i], end=' ')
print()