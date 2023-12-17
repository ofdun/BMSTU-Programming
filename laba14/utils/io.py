import os, struct
from utils.exceptions import NotAnInteger, NotInMenu

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

def writeLine(pathToFile: str, animal: str, height: float, weight: float):
    # little-endian
    line = struct.pack("< 24s f f", animal.encode('cp866'), height, weight)
    with open(pathToFile, "ab") as f:
        f.write(line)
    

# def readFile(pathToFile: str) -> None:
#     with open(pathToFile, 'rb') as file:
#         while True:
#             line = file.read(32)
#             if not line:
#                 break
#             decoded = struct.unpack("< 24s f f", line)
#             animal = decoded[0].decode("cp866")
#             print(animal, f"{decoded[1]:.5g}", f"{decoded[2]:.5g}")
            
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
            if not line:
                break
            line = struct.unpack("< 24s f f", line)
            animal, height, weight = line[0].decode("cp866").strip(), line[1], line[2]
            print(f"|{animal:^38}|",
                  f"{height:^38.5g} |",
                  f"{weight:^38.5g} |", sep="")
            print("-" * WIDTH)