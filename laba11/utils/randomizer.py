from random import randint
     
def createRandomList(n) -> list[int]:
    """
    Создает список из натуральных чисел от 1 до 10**10 с заданной длиной n
    """
    lst = [0]*n
    for i in range(n):
        lst[i] = randint(1, 10**10)
    return lst