import os, struct
from utils.exceptions import NotAnInteger, NotInMenu, NegativeNumberError


def printMenu() -> None:
    MENU="""
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных
5. Удалить произвольную запись из базы данных
6. Поиск по одному полю
7. Поиск по двум полям
0. Завершение программы
"""
    print(MENU)
    
    
def getResponse() -> str:
    while True:
        response = input("Выберете пункт меню: ")
        try:
            response = float(response)
            if int(response) != float(response):
                raise NotAnInteger
            if not(0 <= response <= 7):
                raise NotInMenu
            return response
        except ValueError:
            print("Введенное должно быть числом!\n")
        except NotAnInteger:
            print("Введенное число должно быть целым\n")
        except NotInMenu:
            print("Такого пункта не в меню!\n")
    
    
def confirmRewrite() -> bool:
    while True:
        agreement = input("Вы уверены, что хотите перезаписать файл? (Y/N): ")
        if agreement == "Y" or agreement == "N":
            return agreement == "Y"
    
    
def createFile(pathToFile: str) -> None:
    with open(pathToFile, "wb"):
        return
    

def chooseFile(pathToFile: str) -> [str, bool, bool]:
    try:
        with open(pathToFile, "rb"):
            return pathToFile, True, os.access(pathToFile, os.W_OK)
    except FileNotFoundError:
        return "", False, False
    except PermissionError:
        return pathToFile, False, os.access(pathToFile, os.W_OK)
        
            
def printHeader(width: int):
    print("-" * width)
    HEADERS = ("Животное", "Рост(м)", "Вес(кг)")
    print("|", end="")
    for elem in HEADERS:
        print(f"{elem:^38}| ", end="")
    print()
            

def printDb(pathToFile: str) -> None:
    WIDTH = 120
    printHeader(WIDTH)
    print("-" * WIDTH)
    with open(pathToFile, "rb") as f:
        while True:
            line = f.read(32)
            if len(line) != 32:
                break
            line = struct.unpack("< 24s f f", line)
            animal, height, weight = line[0].rstrip(b"\x00").decode("cp866"), line[1], line[2]
            print(f"|{animal:^38}|",
                  f"{height:^38.5g} |",
                  f"{weight:^38.5g} |", sep="")
            print("-" * WIDTH)
            
            
def chooseField() -> int:
    while True:
        field = input("Введите по какому полю искать: Животное(1), Рост(2), Вес(3): ")
        try:
            if 1 <= int(field) <= 3:
                return int(field)
        except ValueError:
            print("Введено неверное значение! ")
        else:
            print("Введено неверное значение! ")


def enterValue(field: int) -> str | float:
    while True:
        value = input("Введите значение: ")
        if field == 1:
            return value
        try:
            return float(value)
        except ValueError:
            print("Введенное должно быть числом")
            
            
def findByFieldAndPrint(path: str, field: int, value: float | str):
    WIDTH = 120
    printHeader(WIDTH)
    print("-" * WIDTH)
    with open(path, "rb") as f:
        while True:
            line = f.read(32)
            if len(line) != 32:
                break
            line = struct.unpack("< 24s f f", line)
            fields = (line[0].rstrip(b"\x00").decode("cp866"), line[1], line[2])
            if equals(fields[field - 1], value):
                print(f"|{fields[0]:^38}|",
                    f"{fields[1]:^38.5g} |",
                    f"{fields[2]:^38.5g} |", sep="")
                print("-" * WIDTH)
                    
                    
def equals(obj1: str | float, obj2: str | float):
    EPS = 1e-5
    if isinstance(obj1, str):
        return obj1 == obj2
    else:
        return abs(obj1 - obj2) < EPS
                    
                    
def findBy2FieldsAndPrint(path: str, fieldsToFind: [int, int],
                                     values: [str | float, str | float]):
    WIDTH = 120
    printHeader(WIDTH)
    print("-" * WIDTH)
    with open(path, 'rb') as f:
        while True:
            line = f.read(32)
            if len(line) != 32:
                break
            line = struct.unpack("< 24s f f", line)
            fields = (line[0].rstrip(b"\x00").decode("cp866"), line[1], line[2])
            if equals(fields[fieldsToFind[0] - 1], values[0])\
                and equals(fields[fieldsToFind[1] - 1], values[1]):
                print(f"|{fields[0]:^38}|",
                    f"{fields[1]:^38.5g} |",
                    f"{fields[2]:^38.5g} |", sep="")
                print("-" * WIDTH)
                
                
def inputInt(prompt: str) -> int:
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if int(value) == value:
                if value > 0:
                    return int(value)
                else:
                    raise NegativeNumberError
            else:
                raise NotAnInteger
        except ValueError:
            print("Введенное значение должно быть числом!")
        except NotAnInteger:
            print("Введенное число должно быть целым!")
        except NegativeNumberError:
            print("Введенное число должно быть больше 0!")
            

def inputFloat(prompt: str) -> float:
    while True:
        number = input(prompt)
        try:
            return float(number)
        except ValueError:
            print("Введенное должно быть числом!")