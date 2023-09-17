# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: Расчёт характеристик шарового слоя по заданному радиусу и двум высотам

# Импортируем число пи из библиотеки math
from math import pi

# Пользователь вводит данные
radius = float(input("Введите радиус: "))
h1 = float(input("Введите высоту1: "))
h2 = float(input("Введите высоту2: "))

if radius <= 0 or h1 < 0 or h2 < 0 or (h1 == 0 and h2 == 0):
    print("Ошибка! Некорректный ввод!")
else:
    # Найдем расстояние между двумя плоскостями
    h = h1 + h2

    # Найдем радиус первого сечения
    r1 = (radius**2 - h1**2) ** 0.5

    # Найдем радиус второго сечения
    r2 = (radius**2 - h2**2) ** 0.5

    # Расчитаем площадь боковой поверхности шарового слоя
    S_side = 2 * pi * radius * h

    # Расчитаем площадь общей поверхностей шарового слоя
    S_total_surface = S_side + r1**2 * pi + r2**2 * pi

    # Расчитаем объем шарового слоя
    V = 0.5 * pi * h * (r1**2 + r2**2 + h**2 / 3)

    # Выведем результат
    print(
        f"Объем шарового слоя: {V:.5g}",
        f"Площадь боковой поворхности шарового слоя: {S_side:.5g}",
        f"Площадь полной поверхности шарового слоя: {S_total_surface:.5g}",
        sep="\n")