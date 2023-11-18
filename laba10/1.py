# Калашников Елисей ИУ7-15Б
# программу для вычисления приближённого значения интеграла
# известной, заданной в программе, функции двумя разными методами:
# срединных прямоугольников u парабол
from typing import Callable, Tuple

def f(x: float) -> float:
    return x**2


def F(x: float) -> float:
    return x**3/3


def integralUsingNewtonLeibnizMethod(primitiveFunc: Callable, start: float, end: float) -> float:
    return primitiveFunc(end) - primitiveFunc(start)


def inputIsFloat(input_str: str) -> [float, bool]:
    number = 0
    try:
        number = float(input_str)
    except ValueError:
        return number, False
    return number, True


def inputIsInt(input_str: str) -> [int, bool]:
    number = 0
    try:
        number = int(input_str)
    except ValueError:
        return number, False
    return number, True
    

def inputFloat(inputMsg: str) -> float:
    while True:
        number, validated = inputIsFloat(input(inputMsg))
        if validated:
            return number
        print("Введенное значение должно быть числом!")


def inputEvenInt(inputMsg: str) -> int:
    while True:
        number, validated = inputIsInt(input(inputMsg))
        if validated:
            if number % 2 == 0:
                return number 
            print("Введенное значение должно быть четным!")
        print("Введенное значение должно быть целым числом!")


def intergalUsingParabolaMethod(start: float, end: float,
                               n: int) -> float:
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
    print(f"Наиболее плохой метод: {method}")
    print(f"Вычисленное значение интеграла с точностью {eps} = \
{integral:.5g} было достигнуто за {n} интераций")


def main():
    start, end = inputFloat("Введите старт: "), inputFloat("Введите конец: ")
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
    
    if rectanglesMethodInaccuracies[0] < parabolaMethodInaccuracies[0]:
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