# Калашников Елисей ИУ7-15Б
# Добавить удвоенное число после отрицательного в бинарном файле
from utils.io import (inputNums, printFile, writeNums)
from utils.actions import (addDoubled)


def main():
    path = input("Введите путь до файла: ")
    nums = inputNums("Введите числа, которыми вы хотите заполнить файл: ")
    writeNums(path, nums)
    printFile(path)
    addDoubled(path, len(nums))
    printFile(path)

    
if __name__ == '__main__':
    main()