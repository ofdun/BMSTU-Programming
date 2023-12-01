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
        helpString = ""
        pointer = 0
        while pointer != len(line):
            if line[pointer] == subString[0]:
                breaked = False
                for i in range(1, len(subString)):
                    if line[pointer + 1] != subString[i]:
                        breaked = True
                        break
                    helpString += line[pointer]
                    pointer += 1
                if not breaked:
                    newLine += replacementString
                    pointer += 1
                if breaked:
                    newLine += helpString
            newLine += line[pointer]
            pointer += 1
        newText.append(newLine)
    return newText


def countWords(line):
    return len(line.split())


def findSentenceWithLeastWords(text: list[str]) -> [str, int]:
    minWords = float("+inf")
    sentence = ""
    shortestSentence = ""
    words = 0
    i = 1
    for line in text:
        for word in line.split():
            words += 1
            if word[-1] == '.':
                sentence += f"{word}."
                if words < minWords:
                    minWords = words
                    shortestSentence = sentence
                    shortestSentenceIndex = i
                i += 1
                sentence = ""
                print(words)
                words = 0
            else:
                sentence += f"{word} "
    if words < minWords:
        minWords = words
    return shortestSentence, shortestSentenceIndex


def validateMathString(mathString: str) -> bool:
    for i in range(1, len(mathString)):
        substr = mathString[i - 1] + mathString[i]
        if not(substr[0].isdigit() or substr[1].isdigit()):
            if substr not in ("/+", "/-", "*-", "*+"):
                return False
    return True
    
    
def getMathString(line: str, pointer: int) -> [str, bool]:
    mathString = ""
    defaultPointer = pointer
    while pointer < len(line):
        if line[pointer].isdigit() or line[pointer] in '+-/*':
            if pointer != len(line) - 1 and line[pointer] in '+-/*' and not line[pointer + 1].isdigit():
                pointer -= 1
                break
            mathString += line[pointer]
        else:
            break
        pointer += 1
        
    valid = validateMathString(mathString)
    if not valid:
        return "", 0, False

    return mathString, pointer - defaultPointer, True


def product(numbers: list[float]) -> float:
    res = 1
    for number in numbers:
        res *= number
    return res

def evalMathString(mathString: str) -> [float, bool]:
    """
    Returns number: int, exists: bool
    """
    numbers = []
    
    string = ""
    isDivisor = False
    for c in mathString:
        if c == '*' or c == '/':
            if string != "":
                if isDivisor:
                    if string == '0':
                        return 0, False
                    numbers.append(1/float(string))
                numbers.append(float(string))
                string = ""
            isDivisor = c == '/'
        else:
            string += c
    if isDivisor:
        if string == '0':
            return 0, False
        numbers.append(1/float(string))
    else:
        numbers.append(float(string))
    
    if len(numbers) == 1:
        return 0, False
    
    res = product(numbers)
    print(res)
    return res, True


# def a(line: str, pointer: int) -> [list[int], int, bool]:
    # """
    # return expression, offset of pointer, true if exists
    # """
    ...
    # numbers = []
    # defaultPointer = pointer
    # while pointer < len(line):
    #     number = 0
    #     numberExists = False
    #     isNumber = False
    #     if pointer == 0:
    #         isNumber = True
    #     elif line[pointer - 1] in '+- ':
    #         if line[pointer - 1] in "+-":
    #             if pointer == 1 or not line[pointer - 2].isalpha():
    #                 isNumber = True
    #         else:
    #             isNumber = True
    #     elif len(numbers) > 0 and line[pointer - 1] in '*/':
    #         isNumber = True
    #         pointer += 1
    #     while pointer < len(line) and line[pointer].isdigit() and isNumber:
    #         number = number * 10 + int(line[pointer])
    #         numberExists = True
    #         pointer += 1
    #     else:
    #         if pointer == len(line):
    #             if numberExists:
    #                 if line[pointer - len(str(number)) - 1] == '/':
    #                     numbers.append(1/number)
    #                 elif line[pointer - len(str(number)) - 1] == '*':
    #                     numbers.append(number)
    #             elif len(numbers) > 1:
    #                 return numbers, pointer - defaultPointer, True
    #             else:
    #                 return [0], 0, False
    #         elif numberExists:
    #             if line[pointer] == '' or line[pointer] in "*/ ":
    #                 if pointer > len(str(number)):
    #                     if line[pointer - len(str(number))] == '/':
    #                         numbers.append(1/number)
    #                     elif line[pointer - len(str(number))] == '*':
    #                         numbers.append(number)
    #                 else:
    #                     numbers.append(number)
    #             elif len(numbers) > 1:
    #                 return numbers, pointer - defaultPointer, True
    #             else:
    #                 numbers.clear()
    #         pointer += 1
            
    # print(numbers)
            
    
    # return "", 0, False


def multiplyOrDivideInText(text: list[str]) -> list[str]:
    newText = []
    for line in text:
        string = ""
        pointer = 0
        while pointer < len(line):
            offset = 0
            res = None
            exists = False
            c = line[pointer]
            if c.isdigit():
                exp, offset, exists = getMathString(line, pointer)
                if exists:
                    res, exists = evalMathString(exp)
                    if exists:
                        pointer += offset
            if exists:
                string += f"{res:.5g}"
            else:
                string += c
            pointer += 1
        newText.append(string)
                        
    return newText