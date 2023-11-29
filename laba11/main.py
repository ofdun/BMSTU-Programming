# Калашников Елисей ИУ7-15Б
# 1. сначала отсортировать заданный пользователем массив для доказательства корректности работы алгоритма;
# 2. затем составить таблицу замеров времени сортировки списков трёх различных
# (заданных пользователем) размерностей и количества перестановок в каждом из них.
# В части 2 для каждой размерности списка необходимо исследовать:
# ● случайный список,
# ● отсортированный список,
# ● список, отсортированный в обратном порядке.

from utils.inputer import inputInt, inputList
from utils.randomizer import createRandomList
from utils.printer import printHeader, printList, printTable
from utils.sorter import gnome_sort
from copy import deepcopy

def main():
    WIDTH = 147
    
    # Вводим список пользователя и сортируем
    lst = inputList()
    _, _, lst = gnome_sort(lst)
    printList(lst)
    
    # Вводим n1, n2, n3
    n1, n2, n3 = inputInt('1'), inputInt('2'), inputInt('3')
    
    # Заводим списки строк в таблице
    orderedListsList = ["Упор. список"]
    randomListsList = ["Случайный список"]
    backwardsListsList = ["Уп. в обр. порядке"]
    
    for n in n1, n2, n3:
        # Создаем рандомный список
        randList = createRandomList(n)
        # Сортируем его => получаем время и перестановки для рандомного листа
        t, k, orderedRandList = gnome_sort(deepcopy(randList))
        # Сортируем рандомный лист в обратном порядке
        _, _, backwardsRandList = gnome_sort(deepcopy(randList), reverse=True)
        
        # Сортируем упорядоченный список и получаем время и перестановки
        t1, k1, _ = gnome_sort(deepcopy(orderedRandList))
        # Сортируем обратно упорядоченный список и получаем время и перестановки
        t2, k2, _ = gnome_sort(deepcopy(backwardsRandList))
        
        # Заполняем строки для вывода
        orderedListsList.extend([t1, k1])
        randomListsList.extend([t, k])
        backwardsListsList.extend([t2, k2])
        
    # Выводим заголовок и таблицу
    printHeader(WIDTH, n1, n2, n3)
    printTable(WIDTH, [
        ["", "Время", "Перестановок", "Время", "Перестановок", "Время", "Перестановок"],
        orderedListsList,
        randomListsList,
        backwardsListsList
        ])


if __name__ == '__main__':
    main()
