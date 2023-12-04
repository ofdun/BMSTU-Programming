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