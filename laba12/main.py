from utils.io import inputText, getUsersChoiceFromMenu, printText
from utils.actions import (allignLeft, allignRight,
    allignWidth, replaceSubstringInText, findSentenceWithLeastWords,
    multiplyOrDivideInText)

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
                text = replaceSubstringInText(text, wordToReplace, "")
                printText(text)
            case 5:
                wordToReplace = input("Введите слово для замены: ")
                replacementWord = input("Введите слово, которым надо заменить: ")
                text = replaceSubstringInText(text, wordToReplace, replacementWord)
                printText(text)
            case 6:
                text = multiplyOrDivideInText(text)
                printText(text)
            case 7:
                sentenceToDelete, sentenceNumber = findSentenceWithLeastWords(text)
                print(f"Предложение, с наименьшим количеством слов: {sentenceToDelete}")
                # TODO: text = deleteSentence(sentenceNumber)
                printText(text, ignore=sentenceNumber)
            case 0:
                exit(0)
        
        
if __name__ == '__main__':
    main()