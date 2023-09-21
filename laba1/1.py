# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: Расчёт характеристик шарового
# слоя по заданному радиусу и двум высотам

from math import pi # Импортируем число пи из библиотеки math

# Пользователь вводит данные
radius = float(input("Введите радиус: "))
h1 = float(input("Введите высоту1: "))
h2 = float(input("Введите высоту2: "))

# Проверка корректности данных
if radius < 0 or h1 < 0 or h2 < 0 or (h1 == 0 and h2 == 0)\
    or h1 > radius or h2 > radius:
    print("Ошибка! Некорректный ввод!")
else:
    h = h1 + h2     # Найдем расстояние между двумя плоскостями
    r1 = (radius**2 - h1**2) ** 0.5     # Найдем радиус первого сечения
    r2 = (radius**2 - h2**2) ** 0.5     # Найдем радиус второго сечения
    S_side = 2 * pi * radius * h    # Расчитаем площадь боковой поверхности шарового слоя
    S_total_surface = S_side + r1**2 * pi + r2**2 * pi      # Расчитаем площадь общей поверхностей шарового слоя
    V = 0.5 * pi * h * (r1**2 + r2**2 + h**2 / 3)   # Расчитаем объем шарового слоя

    # Выведем результат
    print(
        f"Объем шарового слоя: {V:.5g}",
        f"Площадь боковой поворхности шарового слоя: {S_side:.5g}",
        f"Площадь полной поверхности шарового слоя: {S_total_surface:.5g}",
        sep="\n")
