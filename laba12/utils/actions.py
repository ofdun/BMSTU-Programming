from math import ceil


def allignLeft(text: list[str]) -> list[str]:
    newText = []
    for line in text:
        stringToPrint = ""
        started = False
        for c in line:
            if not started and c.isspace():
                pass
            else:
                stringToPrint += c
                started = True
        newText.append(stringToPrint)
    return newText

def allignRight(text: list[str]) -> list[str]:
    newText = []
    maxLength = 0
    for line in text:
        if len(line) > maxLength:
            maxLength = len(line)
    for line in text:
        newText.append(" " * (maxLength - len(line)) + line)
    return newText

def allignWidth(text: list[str]) -> list[str]:
    newText = []
    maxLength = 0
    for line in text:
        if len(line) > maxLength:
            maxLength = len(line)
    for line in text:
        words = 0
        wasSpace = False
        for c in line:
            if c.isspace():
                wasSpace = True
            elif wasSpace:
                wasSpace = False
                words += 1
        if not line[-1].isspace():
            words += 1
        spacesBetweenWords, additionalSpaces = divmod(maxLength - len(line), words - 1)
        # Учтем изначальный пробел у слов
        spacesBetweenWords += 1
        newString = ""
        wasSpace = False
        for c in line:
            if c.isspace() and not wasSpace:
                newString += " " * spacesBetweenWords
                if additionalSpaces > 0:
                    newString += " "
                    additionalSpaces -= 1
                wasSpace = True
            elif not c.isspace():
                wasSpace = False
                newString += c
            
        newText.append(newString)
    return newText

# def removeAllSubstringsFromText(text: list[str], subString: str) -> list[str]:
#     newText = []
#     for line in text:
#         newLine = ""
#         pointer = 0
#         while pointer != len(line):
#             if line[pointer] == subString[0]:
#                 for j in range(1, len(subString)):
#                     if line[pointer + j] != subString[j]:
#                         break
#                 else:
#                     pointer += len(subString)
#             newLine += line[pointer]
#             pointer += 1
#         newText.append(newLine)
#     return newText

def replaceSubstringInText(text: list[str],
                           subString: str, replacementString: str) -> list[str]:
    newText = []
    for line in text:
        newLine = ""
        pointer = 0
        while pointer != len(line):
            if line[pointer] == subString[0]:
                for i in range(1, len(subString)):
                    if line[pointer + i] != subString[i]:
                        break
                else:
                    newLine += replacementString
                    pointer += len(subString)
            newLine += line[pointer]
            pointer += 1
        newText.append(newLine)
    return newText


def findSentenceWithLeastWords(text: list[str]) -> [str, int]:
    minWords = float("+inf")
    index = 0
    for i, line in enumerate(text):
        words = 0
        wasSpace = False
        for c in line:
            if c.isspace():
                wasSpace = True
            elif wasSpace:
                wasSpace = False
                words += 1
        if not line[-1].isspace():
            words += 1
        if words < minWords:
            minWords = words
            index = i
    return text[index], index