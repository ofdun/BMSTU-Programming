# Калашников

import os
import struct

def printHeader(width: int):
    print("-" * width)
    HEADERS = ("Животное", "Рост(м)", "Вес(кг)")
    print("|", end="")
    for elem in HEADERS:
        print(f"{elem:^38}| ", end="")
    print()


def printLine(line: tuple[str, float, float], width):
    print("-" * width)
    print("|", end="")
    for elem in line:
        print(f"{elem:^38}| ", end="")
    print()
    


def foo(path, stringsToFind: list[str]):
    WIDTH = 120
    printHeader(WIDTH)
    with open(path, "rb") as f:
        while True:
            line = f.read(32)
            if len(line) != 32:
                break
            line = struct.unpack("< 24s f f", line)
            line = line[0].decode("cp866").rstrip("\x00"), line[1], line[2]
            name = line[0]
            for substr in stringsToFind:
                if substr in name:
                    printLine(line, WIDTH)
    print('-' * WIDTH)


def main():
    stringsToFind = input("Введите вхождения, которые необходимо искать через пробел: ").split()
    path = input("Введите путь до базы данных: ")
    if not os.path.exists(path):
        print("Введенная путь невалиден!")
    else:
        foo(path, stringsToFind)


if __name__ == "__main__":
    main()