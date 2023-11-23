from time import time


def timer(func):
    def wrapper(*args, **kwargs) -> [str, list]:
        start = time()
        result = func(*args, **kwargs)
        end = time()
        return f"{(end - start):.5g}", result
    return wrapper


def printTable(w: int, a: [[str]]) -> None:
    print('-'*w)
    for i in range(len(a)):
        cur_width = w // len(a[i])
        string = ''
        for j in range(len(a[i])):
            if isinstance(elem, float):
                elem = f"{elem:.5g}"
            string += "|" + f"{elem:^{cur_width}}"
        print(string + '|')
        print('-'*w)
    


@timer
def gnome_sort(lst: list) -> list:
    n, i = len(lst), 1
    while i < n:
        if i == 0:
            i += 1
        if lst[i] >= lst[i - 1]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst


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
        
    # Ввод элемента 
    while True:
        elem = float(input(f"Введите элемент, который нужно добавить: "))
        if int(elem) != elem:
            print("Значение должно быть цесочисленным")
        else:
            elem = int(elem)
            break
        
    return arr