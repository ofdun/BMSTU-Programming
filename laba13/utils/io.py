from utils.exceptions import NotAnInteger, NotInMenu

def printMenu() -> None:
    MENU="""
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в конец базы данных
5. Поиск по одному полю
6. Поиск по двум полям
0. Завершение программы
"""
    print(MENU)
    

def getAction():
    while True:
        response = input("Выберете пункт меню: ")
        try:
            response = float(response)
            if int(response) != float(response):
                raise NotAnInteger
            if not(0 <= response <= 6):
                raise NotInMenu
            return response
        except ValueError:
            print("Введенное должно быть числом!")
        except NotAnInteger:
            print("Введенное число должно быть целым")
        except NotInMenu:
            print("Такого пункта не в меню!")
            
            
def inputDbPath(prompt: str) -> str:
    while True:
        pathToDb = input(prompt)
        if '\/:*?"<>|' not in pathToDb:
            return pathToDb
        print("Недопустимое название файла!")
        

def inputInt(prompt: str) -> int:
    while True:
        number = input(prompt)
        try:
            number = float(number)
            if int(number) != number:
                raise NotAnInteger
            return int(number)
        except ValueError:
            print("Введенное должно быть числом!")
        except NotAnInteger:
            print("Введенное число должно быть целым")



def inputFloatOrInt(prompt: str) -> float | int:
    while True:
        number = input(prompt)
        try:
            number = float(number)
            if int(number) != number:
                return number
            return int(number)
        except ValueError:
            print("Введенное должно быть числом!")
            

def createDb(path: str, header: str) -> None:
    with open(path, "w", encoding="UTF-8") as f:
        f.write(header + '\n')
        
        
def dbWriteLine(path: str, animal: str) -> None:
    with open(path, "a", encoding="UTF-8") as f:
        f.write(animal + '\n')
        
        
def printDb(path: str) -> None:
    WIDTH = 120
    print("-" * WIDTH)
    with open(path, encoding="UTF-8") as f:
        for line in f:
            string = "|"
            for word in line.split(';'):
                word = word.rstrip()
                if len(word) >= 30:
                    word = word[:27] + "..."
                string += f"{word:^38}| "
            print(string)
            print("-" * WIDTH)
            

def inputAnimal(i: int=-1) -> str:
    if i != -1:
        name = input(f"Введите название животного {i + 1}: ")
        height = str(inputFloatOrInt(f"Введите Рост(м) животного {i + 1}: "))
        weight = str(inputFloatOrInt(f"Введите Вес(кг) животного {i + 1}: "))
    else:
        name = input(f"Введите название животного: ")
        height = str(inputFloatOrInt(f"Введите Рост(м) животного: "))
        weight = str(inputFloatOrInt(f"Введите Вес(кг) животного: "))
    animal = f"{name};{height};{weight}"
    return animal


def inputField() -> int:
    while True:
        field = input("Введите по какому полю искать: Животное(1), Рост(2), Вес(3): ")
        if "1" <= field <= "3":
            return int(field) - 1
        print("Такого поля не существует!")
        
        
def printDataByField(path: str, field: int, query: str) -> None:
    WIDTH = 120
    print("-" * WIDTH)
    with open(path, encoding="UTF-8") as f:
        for i, line in enumerate(f):
            string = "|"
            line = line.split(';')
            if line[field].rstrip() == query or i == 0:
                for word in line:
                    word = word.rstrip()
                    if len(word) >= 30:
                        word = word[:27] + "..."
                    string += f"{word:^38}| "
                print(string)
                print("-" * WIDTH)
                
                
def printDataByTwoFields(path: str, field:  int, query:  str,
                                    field2: int, query2: str) -> None:
    WIDTH = 120
    print("-" * WIDTH)
    with open(path, encoding="UTF-8") as f:
        for i, line in enumerate(f):
            string = "|"
            line = line.split(';')
            if (line[field].rstrip() == query and line[field2].rstrip() == query2) or i == 0:
                for word in line:
                    word = word.rstrip()
                    if len(word) >= 30:
                        word = word[:27] + "..."
                    string += f"{word:^38}| "
                print(string)
                print("-" * WIDTH)