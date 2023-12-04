def replaceSubstringInText(text: list[str],
                           subString: str, replacementString: str) -> list[str]:
    """
    Заменяем подстроку в тексте алгоритмическим путем
    """
    newText = []
    if not subString:
        return text
    for line in text:
        newLine = ""
        helpString = ""
        pointer = 0
        while pointer != len(line):
            if line[pointer] == subString[0]:
                breaked = False
                helpString = subString[0]
                for i in range(1, len(subString)):
                    if line[pointer + 1] != subString[i]:
                        breaked = True
                        break
                    pointer += 1
                    helpString += line[pointer]
                if not breaked:
                    newLine += replacementString
                    pointer += 1
                if breaked:
                    newLine += helpString
            if pointer != len(line):
                newLine += line[pointer]
                pointer += 1
        newText.append(newLine)
    return newText


def findSentenceWithLeastWords(text: list[str]) -> [str, int]:
    """
    Находит предложение с наименьшим кол-вом слов
    """
    minWords = float("+inf")
    sentence = ""
    shortestSentence = ""
    shortestSentenceIndex = 0
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
                words = 0
            else:
                sentence += f"{word} "
    if words < minWords:
        minWords = words
    return shortestSentence, shortestSentenceIndex


def validateMathString(mathString: str) -> bool:
    """
    Проверяет мат. строку на верность
    """
    for i in range(1, len(mathString)):
        substr = mathString[i - 1] + mathString[i]
        if not(substr[0].isdigit() or substr[1].isdigit()):
            if substr not in ("/+", "/-", "*-", "*+"):
                return False
    return True
    
    
def getMathString(line: str, pointer: int) -> [str, bool]:
    """
    Достает мат. строку из строки
    """
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
    """
    Находит умножение всех элементов списка
    """
    res = 1
    for number in numbers:
        res *= number
    return res


def evalMathString(mathString: str) -> [float, bool]:
    """
    Считает мат. строку
    Возвращает число и bool, сущетсвует ли оно
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


def deleteSentence(text: list[str], sentenceNumber: int) -> list[str]:
    newText = []
    string = ""
    sentenceIndex = 1
    for line in text:
        for c in line:
            if c in ".?!":
                sentenceIndex += 1
            if sentenceIndex != sentenceNumber:
                string += c
        if sentenceIndex != sentenceNumber:
            newText.append(string)
            string = ""
    return newText