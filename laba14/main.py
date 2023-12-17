# TODO
import os
from utils.io import (printMenu, getResponse, chooseFile,
                      createFile, confirmRewrite, printDb)

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
                while True:
                    path = input("Введите путь до файла (q чтобы выйти): ")
                    if path == 'q':
                        break
                    path, _, _ = chooseFile(path)
                    if path:
                        break
                    print("Этого файла не существует!\n")
            case 2:
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
                path, r, _ = chooseFile(path)
                if path:
                    if r:
                        printDb(path)
                    else:
                        print("Выбранный файл не доступен для чтения! ")
                else:
                    print("Выберете пригодный файл для использования! ")
                    
            case 4:
                ...
            case 5:
                ...
            case 6:
                ...
            case 7:
                ...

if __name__ == '__main__':
    main()