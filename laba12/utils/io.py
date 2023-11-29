from utils.exceptions import FloatError, NotInMenuError

def inputText() -> list[str]:
    with open("laba12/input.txt") as f:     
        lines = f.read()
    text = lines.split('\n')
    return text

def validateInput(prompt, start, end) -> int:
    while True:
        try:
            num = float(input(prompt))
            if int(num) != num:
                raise FloatError
            if not(start <= int(num) <= end):
                raise NotInMenuError
            return int(num)
        except FloatError:
            print("Введенное число должно быть целым!")
        except ValueError:
            print("Введенное должно быть числом!")
        except NotInMenuError:
            print("Такого значения нет в меню!")
        

def getUsersChoiceFromMenu() -> int:
    """
    
    """
    prompt = ("""\nМеню:
1. Выровнять текст по левому краю
2. Выровнять текст по правому краю
3. Выровнять текст по ширине
4. Удаление всех вхождений заданного слова
5. Замена одного слова другим во всем тексте
6. ...
7. Самое короткое предложение по кол-ву слов
8. Выход\n""")
    print(prompt)
    res = validateInput("Выберите пункт меню: ", 1, 8)
    return res


def printText(text: list[str], ignore: int = -1) -> None:
    print()
    for i, line in enumerate(text):
        if i != ignore:
            print(line)
    print()