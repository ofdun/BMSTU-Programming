from utils.utils import *
from copy import deepcopy


def main():
    WIDTH = 147
    
    lst = inputList()
    lst = [i for i in range(10, -1, -1)]
    _, _, lst = gnome_sort(lst)
    printList(lst)
    
    n1, n2, n3 = inputInt('1'), inputInt('2'), inputInt('3')
    
    orderedListsList = ["Упор. список"]
    randomListsList = ["Случайный список"]
    backwardsListsList = ["Уп. в обр. порядке"]
    
    for n in n1, n2, n3:
        randList = createRandomList(n)
        t, k, orderedRandList = gnome_sort(deepcopy(randList))
        _, _, backwardsRandList = gnome_sort(deepcopy(randList), reverse=True)
        
        t1, k1, _ = gnome_sort(deepcopy(orderedRandList))
        t2, k2, _ = gnome_sort(deepcopy(backwardsRandList))
        
        orderedListsList.extend([t1, k1])
        randomListsList.extend([t, k])
        backwardsListsList.extend([t2, k2])
        
    printHeader(WIDTH, n1, n2, n3)
    printTable(WIDTH, [
        ["", "Время", "Перестановок", "Время", "Перестановок", "Время", "Перестановок"],
        orderedListsList,
        randomListsList,
        backwardsListsList
        ])


if __name__ == '__main__':
    main()
