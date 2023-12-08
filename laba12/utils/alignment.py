def alignLeft(text: list[str]) -> list[str]:
    text = reduceSpaces(text)
    
    return text


def alignRight(text: list[str]) -> list[str]:
    newText = []
    maxLength = 0
    text = reduceSpaces(text)
    for line in text:
        if len(line) > maxLength:
            maxLength = len(line)
    for line in text:
        newText.append(" " * (maxLength - len(line)) + line)
    return newText


def alignWidth(text: list[str]) -> list[str]:
    newText = []
    maxLength = 0
    text = reduceSpaces(text)
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
        if len(line) > 0 and not line[-1].isspace():
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


def reduceSpaces(text: list[str]) -> list[str]:
    newText = []
    for line in text:
        string = ""
        wasSpace = False
        for i, c in enumerate(line):
            if c == ' ':
                wasSpace = True
            else:
                if wasSpace:
                    string += ' ' + c if string else c
                    wasSpace = False
                else:
                    string += c
        newText.append(string)
    return newText