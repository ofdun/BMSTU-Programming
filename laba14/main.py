# Калашников Елисей ИУ7-15Б
# Действия с бд в бинарном виде
import os
from utils.io import (printMenu, getResponse, chooseFile,
                      createFile, confirmRewrite, printDb,
                      chooseField, enterValue, findByFieldAndPrint,
                      findBy2FieldsAndPrint, inputInt, inputFloat)
from utils.actions import deleteRowFromDb, insertRowInDb


def main():
    response = True
    path = ""
    r = w = False
    while response:
        printMenu()
        response = getResponse()
        match response:
            case 0:
                break
            case 1:
                os.system("cls")
                while True:
                    path = input("Введите путь до файла (q чтобы выйти): ")
                    if path == 'q':
                        break
                    path, _, _ = chooseFile(path)
                    if path:
                        break
                    print("Этого файла не существует!\n")
            case 2:
                os.system("cls")
                while True:
                    path = input("Введите путь, где необходимо создать файл (q чтобы выйти): ")
                    if path == 'q':
                        break
                    if os.path.exists(path):
                        rewrite = confirmRewrite()
                        if rewrite:
                            createFile(path)
                            break
                    else:
                        createFile(path)
                        break
            case 3:
                os.system("cls")
                path, r, _ = chooseFile(path)
                if path:
                    if r:
                        printDb(path)
                    else:
                        print("Выбранный файл не доступен для чтения! ")
                else:
                    print("Выберете пригодный файл для использования! ")
                    
            case 4:
                os.system("cls")
                path, r, w = chooseFile(path)
                if not path:
                    print("Выберете пригодный файл для использования! ")
                elif not r:
                    print("Выбранный файл не доступен для чтения! ")
                elif not w:
                    print("Выбранный файл не доступен на запись!")
                else:
                    rowIndex = inputInt("Введите номер строки, куда надо вставить запись: ")
                    animal = input("Введите название животного: ")
                    height = inputFloat("Введите рост животного: ")
                    weight = inputFloat("Введите вес животного: ")
                    insertRowInDb(path, rowIndex, (animal, height, weight))
                    printDb(path)
            case 5:
                os.system("cls")
                path, r, w = chooseFile(path)
                if not path:
                    print("Выберете пригодный файл для использования! ")
                elif not r:
                    print("Выбранный файл не доступен для чтения! ")
                elif not w:
                    print("Выбранный файл не доступен на запись!")
                else:
                    row = inputInt("Введите номер записи, которую надо удалить: ")
                    deleteRowFromDb(path, row)
                    printDb(path)
            case 6:
                os.system("cls")
                path, r, _ = chooseFile(path)
                if path:
                    if r:
                        field = chooseField()
                        value = enterValue(field)
                        findByFieldAndPrint(path, field, value)
                    else:
                        print("Выбранный файл не доступен для чтения! ")
                else:
                    print("Выберете пригодный файл для использования! ")
            case 7:
                os.system("cls")
                path, r, _ = chooseFile(path)
                if path:
                    if r:
                        field1 = chooseField()
                        value1 = enterValue(field1)
                        while True:
                            field2 = chooseField()
                            if field2 == field1:
                                print("Поля должны быть разными!")
                                continue
                            value2 = enterValue(field2)
                            break
                        findBy2FieldsAndPrint(path, (field1, field2),
                                                    (value1, value2))
                    else:
                        print("Выбранный файл не доступен для чтения! ")
                else:
                    print("Выберете пригодный файл для использования! ")

if __name__ == '__main__':
    main()