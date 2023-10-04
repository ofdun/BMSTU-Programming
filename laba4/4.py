# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 10
# Назначение программы: выводит таблицы
# значений функций для a1 = g**3 + 6.1g**2 - 35.4x - 25.7
# a2 = g**2 - cos(pi*g)
# a3 = sqrt(a1**2 + a2**2)
# и строит график функции a1 на заданном диапазоне

from math import cos, pi, sqrt

# start_value = float(input('Введите начальное значение g: '))
# end_value = float(input('Введите конечное значение g: '))
# step = float(input('Введите шаг: '))
start_value = -2
end_value = 0.1
step = 0.5

# Храним ответ в отдельной переменной
answer = ''

eps = 1e-8

# Проверка на исключения:
if start_value >= end_value:
    answer = 'Начальное значение должно быть меньше конечного'
elif step <= 0:
    answer = 'Шаг должен быть положительным'
elif (start_value + step - end_value) > eps:
    answer = 'Внутри интервала должно быть хотя бы 2 шага (Заданный шаг слишком большой)'

# Если ошибок нет, то тогда выполнять программу
if not answer:
    n = int((end_value - start_value) / step) + 1
    
    # Вывод таблицы по центру
    print("-" * 61)
    print(f'| {"g":^12} | {"a1":^12} | {"a2":^12} | {"a3":^12} |')
    print("-" * 61)
    
    current_value = start_value - step
    
    for _ in range(n):
        current_value += step
        a1 = current_value**3  + 6.1*current_value**2 - 35.4*current_value - 25.7
        a2 = current_value**2 - cos(pi*current_value)
        a3 = sqrt(a1**2 + a2**2)
        print(f'| {current_value:^12.5g} | {a1:^12.5g} | {a2:^12.5g} | {a3:^12.5g} |')
    
    print("-" * 61)
else:
    print(answer)





