from time import time
from random import randint


def timer(func):
    def wrapper(*args, **kwargs) -> [str, list]:
        start = time()
        result = func(*args, **kwargs)
        end = time()
        return f"{(end - start):.5g} секунд", *result
    return wrapper


def printTable(w: int, a: [[str]]) -> None:
    print('-'*w)
    for i in range(len(a)):
        cur_width = (w - len(a[i])) // len(a[i])
        string = ''
        for j in range(len(a[i])):
            if isinstance(a[i][j], float):
                a[i][j] = f"{a[i][j]:.5g}"
            if j == len(a[i]) - 1:
                string += "|" + f"{a[i][j]:^{cur_width - 1}}|"
            else:
                string += "|" + f"{a[i][j]:^{cur_width}}"
            
        print(string)
        print('-'*w)
    

@timer
def gnome_sort(lst: list, reverse=False) -> [int, list]:
    countShifts = 0
    n, i = len(lst), 1
    while i < n:
        if i == 0:
            i += 1
        if (lst[i] >= lst[i - 1] and not reverse)\
            or (lst[i] <= lst[i - 1] and reverse):
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            countShifts += 1
            i -= 1
    return countShifts, lst


def inputList() -> list:
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
        
    return arr


def printList(lst: list) -> None:
    print("Итоговый список: ")
    for c in lst:
        print(c, end=' ')
    print()
    
    
def createRandomList(n) -> list[int]:
    lst = [0]*n
    for i in range(n):
        lst[i] = randint(1, 10**10)
    return lst


def inputInt(id: str) -> int:
    while True:
        try:
            n = int(input(f"Введите N{id}: "))
            if n > 0:
                return n
            print("Введенное число должно быть натуральным! ")
        except ValueError:
            print("Введенное число должно быть целым! ")


def printHeader(w:int, n1: int, n2: int, n3: int) -> None:
    print('-'*w)
    print('|' + ' '*20 + '|', end='')
    new_w = w // 3
    for n in n1, n2:
        print(f"{n:^{new_w - 8}.5g}|", end='')
    print(f"{n:^{new_w - 9}.5g}|", end='')
    print()