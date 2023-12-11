import os
from utils.io import (inputDbPath, inputInt,
                      createDb, dbWriteLine,
                      inputAnimal)


def getIfFileExists(path: str) -> bool:
    if path[-4:] != '.txt':
        return False
    try:
        with open(path) as _:
            return True
    except FileNotFoundError:
        return False
    
    
def getIfFileIsReadable(path: str) -> bool:
    return os.access(path, os.R_OK)


def getIfFileIsWriteable(path: str) -> bool:
    return os.access(path, os.W_OK)


def getIfItIsDB(path: str) -> bool:
    with open(path, encoding="UTF-8") as f:
        for i, line in enumerate(f):
            if i == 0:
                if line.rstrip() != "Животное;Рост(м);Вес(кг)":
                    return False
                continue
            splittedLine = line.split(";")
            if len(splittedLine) != 3:
                return False
            for j in range(1, 3):
                try:
                    float(splittedLine[j])
                except ValueError:
                    return False            
    return True


def chooseWorkingFile(path: str) -> [str, bool]:
    fileExists = getIfFileExists(path)
    fileIsReadable = getIfFileIsReadable(path) if fileExists else False
    fileIsWriteable = getIfFileIsWriteable(path) if fileExists else False
    fileIsDb = getIfItIsDB(path) if fileExists and fileIsReadable else False
    if fileExists and fileIsReadable and fileIsDb:
        return path, fileIsWriteable
    else:
        if not fileExists:
            print("Файл не найден!")
        elif not fileIsReadable:
            print("Файл не доступен для чтения!")
        elif not fileIsDb:
            print("Выбранный файл не является подходящей базой данных для данной программы!")
        return "", False
    

def choosePathToDb(prompt: str) -> str:
    while True:
        pathToDb = inputDbPath(prompt)
        pathToDb, writeable = chooseWorkingFile(pathToDb)
        if pathToDb != "":
            return pathToDb, writeable
        
        
def initDb(path: str) -> None:
    if path[-4:] != '.txt':
        path += '.txt'
    
    headers = "Животное;Рост(м);Вес(кг)"
    animals = []
    n = inputInt("Введите кол-во строк, которые вы хотите ввести: ")
    for i in range(n):
        animal = inputAnimal(i)
        animals.append(animal)
        
    createDb(path, headers)
    for animal in animals:
        dbWriteLine(path, animal)