# Калашников Елисей ИУ7-15Б
# Отсортировать числа в файле с помощью гномьей сортировки
from utils.io import (inputNums, printFile, writeNums)
from utils.actions import (gnomeSortFile)


def main():
    path = input("Введите путь до файла: ")
    nums = inputNums("Введите числа, которыми вы хотите заполнить файл: ")
    writeNums(path, nums)
    printFile(path)
    gnomeSortFile(path, len(nums))
    printFile(path)
    
    
if __name__ == "__main__":
    main()
