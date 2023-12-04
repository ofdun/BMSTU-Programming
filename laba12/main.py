# Калашников Елисей ИУ7-15Б
# Программа должна позволять с помощью меню выполнить следующие действия:
# 1. Выровнять текст по левому краю.
# 2. Выровнять текст по правому краю.
# 3. Выровнять текст по ширине.
# 4. Удаление всех вхождений заданного слова.
# 5. Замена одного слова другим во всём тексте.
# 6. Вычисление арифметических выражений над целыми числами внутри текста
# (по варианту).
# 7. Найти (вывести на экран) и затем удалить слово или предложение по варианту.
from utils.io import inputText, getUsersChoiceFromMenu, printText
from utils.allignment import allignLeft, allignRight,allignWidth
from utils.actions import (replaceSubstringInText, findSentenceWithLeastWords,
    multiplyOrDivideInText, deleteSentence)

def main():
    # Ввод текста
    text = inputText()
    while True:
        # Получение ответа от меню
        response = getUsersChoiceFromMenu()
        match response:
            case 1:
                # Выравнивание по левому краю
                newText = allignLeft(text)
                printText(newText)
            case 2:
                # Выравнивание по правому краю
                newText = allignRight(text)
                printText(newText)
            case 3:
                # Выравнивание по ширине
                newText = allignWidth(text)
                printText(newText)
            case 4:
                # Удаляем вхождения введенного слова
                wordToReplace = input("Введите слово для удаления: ")
                text = replaceSubstringInText(text, wordToReplace, "")
                printText(text)
            case 5:
                # Заменяем вхождения слова на другое
                wordToReplace = input("Введите слово для замены: ")
                replacementWord = input("Введите слово, которым надо заменить: ")
                text = replaceSubstringInText(text, wordToReplace, replacementWord)
                printText(text)
            case 6:
                # Делаем мат. действия в тексте
                text = multiplyOrDivideInText(text)
                printText(text)
            case 7:
                # Удаляем предложение с наим. кол-вом слово
                sentenceToDelete, sentenceNumber = findSentenceWithLeastWords(text)
                print(f"Предложение, с наименьшим количеством слов: {sentenceToDelete}")
                text = deleteSentence(text, sentenceNumber)
                if text[0] == '.':
                    print("Предложений не осталось")
                    exit(1)
                printText(text)
            case 0:
                # Выход из программы
                exit(0)
        
        
if __name__ == '__main__':
    main()

