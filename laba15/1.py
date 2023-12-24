# Калашников Елисей ИУ7-15Б
# Удалить все отрицательные числа из файла
from utils.io import (inputNums, printFile, writeNums)
from utils.actions import (removeNegatives)


def main():
    path = input("Введите путь до файла: ")
    nums = inputNums("Введите числа, которыми вы хотите заполнить файл: ")
    writeNums(path, nums)
    printFile(path)
    removeNegatives(path, len(nums))
    printFile(path)
    
    
if __name__ == '__main__':
    main()
    