from utils.timer_ import timer

@timer
def gnome_sort(lst: list, reverse=False) -> [int, list]:
    """
    Сортирует список методом гнимьей сортировки
    """
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
