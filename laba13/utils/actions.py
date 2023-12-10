import os
from utils.io import (inputDbPath, inputInt,
                      createDb, dbWriteLine,
                      inputAnimal)


def getIfFileExists(path: str) -> bool:
    os.path.abspath(__name__)
    if path[-4:] != '.txt':
        return False
    try:
        with open(path) as _:
            return True
    except FileNotFoundError:
        return False
    
    
def getIfFileIsReadable(path: str) -> bool:
    return os.access(path, os.R_OK)


def chooseWorkingFile(path: str) -> str:
    if getIfFileExists(path) and getIfFileIsReadable(path):
        return path
    else:
        if not getIfFileExists(path):
            print("Файл не найден!")
        elif not getIfFileIsReadable(path):
            print("Файл не доступен для чтения!")
        return ""
    

def choosePathToDb(prompt: str) -> str:
    while True:
        pathToDb = inputDbPath(prompt)
        pathToDb = chooseWorkingFile(pathToDb)
        if pathToDb != "":
            return pathToDb
        
        
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