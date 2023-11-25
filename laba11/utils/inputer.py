def inputList() -> list:
    """
    Ввод списка через stdin
    """
    # Ввод длины списка
    while True:
        n = input('Введите длину списка: ')
        try:
            n = float(n)
            if n > 0  and int(n) == n:
                n = int(n)
                break
            print("Число должно быть натуральным")
        except ValueError:
            print("Длина списка должна быть натуральной")

    arr = []

    # Ввод списка
    for i in range(n):
        while True:
            elem = input(f"Введите {i + 1} элемент массива: ")
            try:
                elem = float(elem)
                if elem == int(elem):
                    elem = int(elem)
                    arr.append(elem)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Значение должно быть целочисленным")
                
        
    return arr


def inputInt(id: str) -> int:
    """
    Ввод int через stdin
    """
    while True:
        try:
            n = float(input(f"Введите N{id}: "))
            if n > 0 and int(n) == n:
                return int(n)
            print("Введенное число должно быть натуральным! ")
        except ValueError:
            print("Введенное число должно быть целым! ")
            