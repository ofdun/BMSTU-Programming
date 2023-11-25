def printHeader(w:int, n1: int, n2: int, n3: int) -> None:
    """
    Выводит заголовок
    """
    print('-'*w)
    print('|' + ' '*20 + '|', end='')
    new_w = w // 3
    for n in n1, n2:
        print(f"{n:^{new_w - 8}.5g}|", end='')
    print(f"{n3:^{new_w - 9}.5g}|", end='')
    print()
    
    
def printList(lst: list) -> None:
    """
    Выводит список
    """
    print("Итоговый список: ", end='')
    for c in lst:
        print(c, end=' ')
    print()
    

def printTable(w: int, a: [[str]]) -> None:
    """
    Выводит таблицу
    """
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
        