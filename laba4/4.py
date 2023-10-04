# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 10
# Назначение программы: выводит таблицы
# значений функций для a1 = g**3 + 6.1g**2 - 35.4x - 25.7
# a2 = g**2 - cos(pi*g)
# a3 = sqrt(a1**2 + a2**2)
# и строит график функции a1 на заданном диапазоне

from math import cos, pi, sqrt, inf

# start_value = float(input('Введите начальное значение g: '))
# end_value = float(input('Введите конечное значение g: '))
# step = float(input('Введите шаг: '))
start_value = -2
end_value = 0
step = 0.5
scale = 8 # засечки

# Храним ответ в отдельной переменной
answer = ''

eps = 1e-8
count_positive = 0 # считаем положительные значения a2 для доп задания
first_elem_of_func = None # Найдем первое значение функции
a1_max = -inf
a1_min = inf

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
        # для доп задания
        if a2 > eps:
            count_positive += 1
        a1_max = max(a1_max, a1)
        a1_min = min(a1_min, a1)
        if first_elem_of_func is None:
            first_elem_of_func = a1
    
    # Отделим график от таблицы
    print('\n\n')
    
    # Выводим верх таблицы
    width = 80 # Ширина
    scale_step = (a1_max - a1_min) / (scale - 1)
    space_between_scale = int((width - 10) / scale)
    top_prompt = ' '*10
    
    current_scale = a1_min - scale_step
    for _ in range(scale):
        current_scale += scale_step
        top_prompt += f"{current_scale:<10.5g}"
    
    print(top_prompt)
    
    median_of_func = abs(a1_min - a1_max)
    current_value = start_value - step
    for _ in range(n):
        current_value += step
        a1 = current_value**3  + 6.1*current_value**2 - 35.4*current_value - 25.7
        point_min_median = abs(a1_min - a1)
        offset = int((point_min_median / median_of_func) * (width - 10))
        prompt = f"{current_value:<8.5g} |{' '*offset}*"
        print(prompt)
        
else:
    print(answer)
