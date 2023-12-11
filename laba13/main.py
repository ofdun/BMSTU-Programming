# Калашников Елисей ИУ7-15Б
# Назначение программы: работа с элементарными базами данных в txt файле
from utils.io import (printMenu, getAction, inputDbPath,
                      printDb, inputAnimal, dbWriteLine,
                      inputField, printDataByField, printDataByTwoFields)
from utils.actions import choosePathToDb, initDb


def main():
    pathToDb = ""
    while True:
        printMenu()
        action = getAction()
        match action:
            case 0:
                break
            case 1:
                pathToDb, writeable = choosePathToDb("Введите путь до базы данных: ")
            case 2:
                prompt = "Введите путь, где необходимо инициализировать базу данных: "
                pathToDb = inputDbPath(prompt)
                initDb(pathToDb)
            case 3:
                if pathToDb:
                    printDb(pathToDb)
                else:
                    print("Сначала выберете базу данных для работы! ")
            case 4:
                if pathToDb and writeable:
                    animal = inputAnimal()
                    dbWriteLine(pathToDb, animal)
                elif not pathToDb:
                    print("Сначала выберете базу данных для работы! ")
                else:
                    print("Нет прав для записи!")
            case 5:
                if pathToDb:
                    field = inputField()
                    query = input("Введите, что вы хотите найти: ")
                    printDataByField(pathToDb, field, query)
                else:
                    print("Сначала выберете базу данных для работы! ")
            case 6:
                if pathToDb:
                    field = inputField()
                    query = input("Введите, что вы хотите найти: ")
                    while True:
                        field2 = inputField()
                        if field2 != field:
                            break
                        print("Поля должны быть разными!")
                    query2 = input("Введите, что вы хотите найти: ")
                    printDataByTwoFields(pathToDb, field, query,
                                                   field2, query2)
                else:
                    print("Сначала выберете базу данных для работы! ")
    
    
if __name__ == '__main__':
    main()