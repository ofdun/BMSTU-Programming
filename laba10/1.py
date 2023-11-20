# Калашников Елисей ИУ7-15Б
# программу для вычисления приближённого значения интеграла
# известной, заданной в программе, функции двумя разными методами:
# срединных прямоугольников u парабол
from typing import Callable, Tuple

def f(x: float) -> float:
    """
    Фунцкия f(x)
    """
    return x**2


def F(x: float) -> float:
    """
    Первообразная функция для f(x)
    """
    return x**3/3


def integralUsingNewtonLeibnizMethod(primitiveFunc: Callable, start: float, end: float) -> float:
    """
    Вычисление интеграла с помощью формулы Ньютона-Лейбница
    """
    return primitiveFunc(end) - primitiveFunc(start)


def inputIsFloat(input_str: str) -> [float, bool]:
    """
    Возвращает (число, True) если строка является float,
    иначе возвращает (0, False)
    """
    # Вводим все переменные
    number = 0
    input_str = str(input_str)
    input_str = input_str.strip()
    digits = set('1234567890')
    characters = set('+-')
    ten_degree = set('eE')
    was_e = False
    dot_count = 0
    e_count = 0
    i = 0

    # Обрабатываем длину
    if len(input_str) == 0:
        return number, False

    # Обрабатываем первый элемент
    if input_str[0] not in digits and input_str[0] not in characters and input_str[0] != '.':
        return number, False
    elif input_str[0] in characters:
        i += 1
    
    # Если длина 1 и элементы '+', '-' или '.'
    if len(input_str) == 1 and (input_str[0] in characters or input_str[0] == '.'):
        return number, False
    
    # Если последний элемент 'e', '+' или '-'
    if input_str[len(input_str) - 1] in ten_degree or input_str[len(input_str) - 1] in characters:
        return number, False

    # Случай '.e_abc' и '+.e_abc'
    if (input_str[0] == '.' and input_str[1] in ten_degree) or (len(input_str) > 2\
        and input_str[0] in characters and input_str[1] == '.' and input_str[2] in ten_degree):
        return number, False

    # Случай 'abc.'
    if input_str[len(input_str) - 1] == '.' and input_str[len(input_str) - 2] not in digits:
        return number, False

    # Проходимся циклом
    while i != len(input_str) - 1:

        # Отбираем только все цифры, '.', '+', '-' и 'e'
        if input_str[i] not in digits and input_str[i] not in characters \
            and input_str[i] not in ten_degree and input_str[i] != '.':
            return number, False
        
        # Если попадется '.' и '+', '-'
        if input_str[i] == '.':
            dot_count += 1
        elif input_str[i] in characters:
            return number, False
        
        # Если находим точку после 'e'
        if was_e == True and dot_count > 0:
            return number, False
        
        # Обрабатываем 'e'
        if input_str[i] in ten_degree:
            e_count += 1
            was_e = True

            # Если перед 'e' есть цифра или '.'
            if input_str[i - 1] not in digits and input_str[i - 1] != '.':
                return number, False

            # Разделяем обработку на 'до e' и 'после e'
            if e_count > 1 or dot_count > 1:
                return number, False
            else:
                dot_count = 0
            
            # Если после 'e' есть '+' или '-'
            if input_str[i + 1] in characters:
                i += 1

        # Обрабатываем случай 'abc_e_dfg.'
        if e_count > 0 and input_str[len(input_str) - 1] == '.':
            return number, False
        
        i += 1      # Инкрементируем счетчик
    
    number = float(input_str)
    return number, True    # Выход


def inputIsInt(input_str: str) -> (int, bool):
    """
    Возвращает (число, True) если оно является int,
    иначе возвращает (0, False)
    """
    number, validated = inputIsFloat(input_str)
    if validated:
        if number == int(number):
            return int(number), True
    return number, False
    

def inputFloat(inputMsg: str) -> float:
    """
    Ввод float числа
    """
    while True:
        number, validated = inputIsFloat(input(inputMsg))
        if validated:
            return number
        print("Введенное значение должно быть числом!")


def inputEvenInt(inputMsg: str) -> int:
    """
    Ввод четного целого числа
    """
    while True:
        number, validated = inputIsInt(input(inputMsg))
        if validated:
            if number % 2 == 0:
                return number 
            print("Введенное значение должно быть четным!")
            continue
        print("Введенное значение должно быть целым числом!")


def intergalUsingParabolaMethod(start: float, end: float,
                               n: int) -> float:
    """
    Вычисление интеграла с помощью метода парабол ( формулы Симпсона )
    """
    if n % 2 != 0:
        return -1
    
    integral = f(start) + f(end)
    
    x = start
    step = (end - start) / n
    #                     n//2               n//2
    # Формула S = h/3[ 4 * Σ [f(x2i-1)] + 2 * Σ [f(x2i)] + f(xn)]
    #                     i=1                i=1
    for i in range(1, n):
        x = start + step * i
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    integral *= step / 3
    return integral
       
        
def integralUsingMiddleSquareMethod(start: float, end: float,
                                    n: int) -> float:
    """
    Вычисление интеграла с помощью метода срединных прямоугольников
    """
    integral = 0
    x = start
    step = (end - start) / n
    for i in range(n):
        height = f(x + step / 2)
        integral += step * height
        x = start + step * i
    return integral


def compareIntegrals(it1: float, it2: float) -> Tuple[float, float]:
    """
    Находит абсолютную и относительную погрешность
    """
    return abs(it2 - it1), abs(1 - (it1 / it2))


def printTable(rectangleIntegrals: Tuple[float, float],
               trapezeIntegrals: Tuple[float, float],
               n1: int, n2: int) -> None:
    print("-"*107)
    print(f"|{'Таблица вычисленных интегралов':^105}|")
    
    print("|" + "-"*105 + "|")
    print(f"|{'Кол-во участков разбиения':^35}|", end="")
    for n in n1, n2:
        print(f"{n:^34}|", end="")
    print("\n|" + "-"*105 + "|")
    
    print(f"|{'Метод срединных прямоугольников':^35}|", end="")
    for integral in rectangleIntegrals:
        print(f"{integral:^34.5g}|", end="")
    print("\n|" + "-"*105 + "|")
    
    print(f"|{'Метод парабол':^35}|", end="")
    for integral in trapezeIntegrals:
        print(f"{integral:^34.5g}|", end="")
    print("\n" + "-"*107)
    
    
def printInaccuraciesTable(rectangleMethodInaccuracies: Tuple[float, float],
                           parabolaMethodInaccuracies: Tuple[float, float],
                           n1: int, n2: int, absolute: bool=True) -> None:
    """
    Выводит таблицу абсолютных погрешностей если absolute=True,
    иначе выводит таблицу относительных погрешностей
    """
    if absolute:
        heading = "Таблица абсолютных погрешностей"
    else:
        heading = "Таблица относительных погрешностей"
        
    print("-"*107)
    print(f"|{heading:^105}|")
    
    print("|" + "-"*105 + "|")
    print(f"|{'Кол-во участков разбиения':^35}|", end="")
    for n in n1, n2:
        print(f"{n:^34}|", end="")
        
    print("\n|" + "-"*105 + "|")
    
    print(f"|{'Метод срединных прямоугольников':^35}|", end="")
    for inacc in rectangleMethodInaccuracies:
        if absolute:
            print(f"{inacc[0]:^34.5g}|", end="")
        else:
            print(f"{inacc[1]:^34.1%}|", end="")
    print("\n|" + "-"*105 + "|")
    
    print(f"|{'Метод парабол':^35}|", end="")
    for inacc in parabolaMethodInaccuracies:
        if absolute:
            print(f"{inacc[0]:^34.5g}|", end="")
        else:
            print(f"{inacc[1]:^34.1%}|", end="")
    print("\n" + "-"*107)
    

def correctIntegral(method: str, start: float, end: float, eps: float) -> Tuple[float, int]:
    """
    Узнает количество итераций для вычисления интеграла с заданной точностью
    Принимает два метода: 'Метод парабол' и 'Метод срединных прямоугольников'
    """
    n = 2
    if method == 'Метод парабол':
        integralFunc = intergalUsingParabolaMethod
    else:
        integralFunc = integralUsingMiddleSquareMethod
    integral = integralFunc(start, end, n)
    doubledIntegral = integralFunc(start, end, n * 2)
    while True:
        if abs(doubledIntegral - integral) - eps < 0:
            return integral, n
        else:
            n *= 2
            integral = doubledIntegral
            doubledIntegral = integralFunc(start, end, n * 2)


def printCorrectedIntegral(integral: float, n: int, eps: float, method: str) -> None:
    """
    Выводит "скорректированный" интеграл
    """
    print(f"Наиболее плохой метод: {method}")
    print(f"Вычисленное значение интеграла с точностью {eps} = \
{integral:.5g} было достигнуто за {n} интераций")


def inputStartAndEnd() -> Tuple[float, float]:
    while True:
        start, end = inputFloat("Введите старт: "), inputFloat("Введите конец: ")
        if end > start:
            return start, end
        print("Ошибка! Конец отрезка интегрирования меньше начала!")


def main():
    start, end = inputStartAndEnd()
    # Метод парабол не работает при нечетных n => запросим только четные n
    n1, n2 = inputEvenInt("Введите N1: "), inputEvenInt("Введите N2: ")
    eps = inputFloat("Введите погрешность: ")
    
    trueIntegral = integralUsingNewtonLeibnizMethod(F, start, end)
    rectanglesIntegrals = (integralUsingMiddleSquareMethod(start, end, n1),
                          integralUsingMiddleSquareMethod(start, end, n2))
    parabolaIntegrals = (intergalUsingParabolaMethod(start, end, n1),
                       intergalUsingParabolaMethod(start, end, n2))
    
    rectanglesMethodInaccuracies = (compareIntegrals(rectanglesIntegrals[0], trueIntegral),
                                       compareIntegrals(rectanglesIntegrals[1], trueIntegral))
    parabolaMethodInaccuracies = (compareIntegrals(parabolaIntegrals[0], trueIntegral),
                                     compareIntegrals(parabolaIntegrals[1], trueIntegral))
    
    if min(rectanglesMethodInaccuracies[0][1], rectanglesMethodInaccuracies[1][1]) < min(
        parabolaMethodInaccuracies[0][1], parabolaMethodInaccuracies[1][1]):
        worseMethod = "Метод парабол"
    else:
        worseMethod = "Метод срединных прямоугольников"
    
    correctedIntegral, n3 = correctIntegral(worseMethod, start, end, eps)
    
    printTable(rectanglesIntegrals, parabolaIntegrals, n1, n2)
    for absolute in True, False:
        printInaccuraciesTable(rectanglesMethodInaccuracies,
                                parabolaMethodInaccuracies,
                                n1, n2, absolute)
    
    printCorrectedIntegral(correctedIntegral, n3, eps, worseMethod)
    
if __name__ == '__main__':
    main()