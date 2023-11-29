from utils.io import inputText, getUsersChoiceFromMenu, printText
from utils.actions import (allignLeft, allignRight,
    allignWidth, replaceSubstringInText, findSentenceWithLeastWords)

def main():
    text = inputText()
    while True:
        response = getUsersChoiceFromMenu()
        match response:
            case 1:
                newText = allignLeft(text)
                printText(newText)
            case 2:
                newText = allignRight(text)
                printText(newText)
            case 3:
                newText = allignWidth(text)
                printText(newText)
            case 4:
                wordToReplace = input("Введите слово для удаления: ")
                newText = replaceSubstringInText(text, wordToReplace, "")
                printText(newText)
            case 5:
                wordToReplace = input("Введите слово для замены: ")
                replacementWord = input("Введите слово, которым надо заменить: ")
                newText = replaceSubstringInText(text, wordToReplace, replacementWord)
                printText(newText)
            case 6:
                ...
            case 7:
                # TOFIX delete from sentence, not line
                sentenceToDelete, index = findSentenceWithLeastWords(text)
                print(f"Предложение, с наименьшим количеством слов: {sentenceToDelete}")
                printText(text, ignore=index)
            case 8:
                exit()
        
        
if __name__ == '__main__':
    main()