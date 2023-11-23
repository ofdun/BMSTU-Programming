# Калашников Елисей ИУ7-15Б
# программу для вычисления приближённого значения интеграла
# известной, заданной в программе, функции двумя разными методами:
# срединных прямоугольников u парабол
from typing import Callable, Tuple, List

from math import log

def f(x: float) -> float:
    """
    Фунцкия f(x)
    """
    return log(x)


def F(x: float) -> float:
    """
    Первообразная функция для f(x)
    """
    return x*(log(x) - 1)


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


def inputIsInt(input_str: str) -> [int, bool]:
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


def inputInt(inputMsg: str) -> int:
    """
    Ввод натурального числа
    """
    while True:
        number, validated = inputIsInt(input(inputMsg))
        if validated:
            if number >= 0:
                return number
        print("Введенное значение должно быть натуральным числом!")


def intergalUsingParabolaMethod(start: float, end: float,
                               n: int) -> float:
    """
    Вычисление интеграла с помощью метода парабол ( формулы Котеса )
    """
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
    for _ in range(n):
        height = f(x + step / 2)
        integral += step * height
        x += step
    return integral


def compareIntegrals(it1: float, it2: float) -> Tuple[float, float]:
    """
    Находит абсолютную и относительную погрешность
    Возвращает (float, -1) если невозможно найти относительную погрешность
    """
    if it2 == 0:
        return abs(it2 - it1), -1
    return abs(it2 - it1), abs(1 - (it1 / it2))

    
def printTable(heading: str, *a: List[str]) -> None:
    """
    Выводит таблицу вида:
    -----------------------------------------------------------------------------------------------------------
    |                                                   name                                                  |
    |---------------------------------------------------------------------------------------------------------|
    |              a[0][0]              |             a[0][1]              |             a[0][2]              |
    |---------------------------------------------------------------------------------------------------------|
    |              a[1][0]              |             a[1][1]              |             a[1][2]              |
    |---------------------------------------------------------------------------------------------------------|
    |                ...                |               ...                |               ...                |
    |---------------------------------------------------------------------------------------------------------|
    |              a[n][0]              |             a[n][1]              |             a[n][2]              |
    -----------------------------------------------------------------------------------------------------------
    """
    print("-"*107)
    print(f"|{heading:^105}|")
    print("-"*107)
    
    for i in range(len(a)):
        print(f"|{a[i][0]:^35}|", end="")
        print(f"{a[i][1]:^34}|", end="")
        print(f"{a[i][2]:^34}|", end="")
        if i != len(a) - 1:
            print('\n' + "-"*107)
    print('\n' + "-"*107)
    

def correctIntegral(integralFunc: Callable, start: float, end: float, eps: float) -> Tuple[float, int]:
    """
    Узнает количество итераций для вычисления интеграла с заданной точностью
    Принимает два метода: 'Метод парабол' и 'Метод срединных прямоугольников'
    """
    n = 2
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
        return start, end
        
def detectWorseMethod(rectInaccuracies: Tuple[Tuple[float]],
                      parabolaInaccuracies: Tuple[Tuple[float]]) -> [Callable, str]:
    if parabolaInaccuracies[0][0] == '-':
        if parabolaInaccuracies[1][0] == '-':
            return integralUsingMiddleSquareMethod, "Метод срединных прямоугольников"
        if rectInaccuracies[1][0] > parabolaInaccuracies[1][0]:
            return integralUsingMiddleSquareMethod, "Метод срединных прямоугольников"
        else:
            return intergalUsingParabolaMethod, "Метод парабол"
    if parabolaInaccuracies[1][0] == '-':
        if parabolaInaccuracies[0][0] == '-':
            return integralUsingMiddleSquareMethod, "Метод срединных прямоугольников"
        if rectInaccuracies[0][0] > parabolaInaccuracies[0][0]:
            return integralUsingMiddleSquareMethod, "Метод срединных прямоугольников"
        else:
            return intergalUsingParabolaMethod, "Метод парабол"
    if min(rectInaccuracies[0][0], rectInaccuracies[1][0]) > min(
        parabolaInaccuracies[0][0], parabolaInaccuracies[1][0]):
        return integralUsingMiddleSquareMethod, "Метод срединных прямоугольников"
    return intergalUsingParabolaMethod, "Метод парабол"


def main():
    start, end = inputStartAndEnd()
    n1, n2 = inputInt("Введите N1: "), inputInt("Введите N2: ")
    
    # Расчитаем интегралы, используя разные методы
    trueIntegral = integralUsingNewtonLeibnizMethod(F, start, end)
    # rectanglesIntegrals и parabolaIntegrals
    # представляют собой вид (интеграл при n1, интеграл при n2)
    rectanglesIntegrals = (integralUsingMiddleSquareMethod(start, end, n1),
                          integralUsingMiddleSquareMethod(start, end, n2))
    parabolaIntegrals = (intergalUsingParabolaMethod(start, end, n1) if n1 % 2 == 0 else '-',
                       intergalUsingParabolaMethod(start, end, n2) if n2 % 2 == 0 else '-')
    
    heading = "Таблица вычисленных интегралов"
    printTable(heading, ["Кол-во участков разбиения", str(n1), str(n2)],
               
               ["Метод срединных прямоугольников",
                f"{rectanglesIntegrals[0]:.5g}", f"{rectanglesIntegrals[1]:.5g}"],
               
               ["Метод парабол",
                parabolaIntegrals[0] if n1 % 2 == 0 else '-',
                parabolaIntegrals[1] if n2 % 2 == 0 else '-'])
    
    # rectanglesMethodInaccuracies и parabolaMethodInaccuracies
    # предсталяют собой (absolute, rel) при n1, (absolute, rel) при n2
    rectanglesMethodInaccuracies = (compareIntegrals(rectanglesIntegrals[0], trueIntegral),
                                       compareIntegrals(rectanglesIntegrals[1], trueIntegral))
    parabolaMethodInaccuracies = (compareIntegrals(parabolaIntegrals[0], trueIntegral) if n1 % 2 == 0 else ('-', '-'),
                                     compareIntegrals(parabolaIntegrals[1], trueIntegral) if n2 % 2 == 0 else ('-', '-'))
    
    # Выводим таблицу абсолютных погрешностей
    heading = "Таблица абсолютных погрешностей"
    printTable(heading, ["Кол-во участков разбиения", str(n1), str(n2)],
               
               ["Метод срединных прямоугольников",
                f"{rectanglesMethodInaccuracies[0][0]:.5g}", f"{rectanglesMethodInaccuracies[1][0]:.5g}"],
               
               ["Метод парабол",
                f"{parabolaMethodInaccuracies[0][0]:.5g}" if n1 % 2 == 0 else '-',
                f"{parabolaMethodInaccuracies[1][0]:.5g}" if n2 % 2 == 0 else '-'])
    
    worseMethodFunc, worseMethod = detectWorseMethod(rectanglesMethodInaccuracies,
                                      parabolaMethodInaccuracies)
    
    if rectanglesMethodInaccuracies[1][1] == -1 or rectanglesMethodInaccuracies[0][1] == -1 or\
        parabolaMethodInaccuracies[1][1] == -1 or parabolaMethodInaccuracies[0][1] == -1:
        print("Невозможно вычислить относительные погрешности!")
    else:
        heading = 'Таблица относительных погрешностей'
        printTable(heading, ["Кол-во участков разбиения", str(n1), str(n2)],
                ["Метод срединных прямоугольников",
                    f"{rectanglesMethodInaccuracies[0][1]:.5g}",
                    f"{rectanglesMethodInaccuracies[1][1]:.5g}"],
                ["Метод парабол",
                    f"{parabolaMethodInaccuracies[0][1]:.5g}" if n1 % 2 == 0 else '-',
                    f"{parabolaMethodInaccuracies[1][1]:.5g}" if n2 % 2 == 0 else '-'])
        
    eps = inputFloat("Введите погрешность: ")
    correctedIntegral, n3 = correctIntegral(worseMethodFunc, start, end, eps)
    printCorrectedIntegral(correctedIntegral, n3, eps, worseMethod)
    
if __name__ == '__main__':
    main()