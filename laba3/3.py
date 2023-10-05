# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Назначение программы: по введенным целочисленным
# координатам трех точек на плоскости вычисляет длины сторон
# образованного треугольника и длину высоты, проведенной из
# наибольшего угла. Определяет, является ли треугольник прямоугольным.
# По введенной координате точки определяет, находится ли она внутри него
# и кратчайшее расстояние до стороны

# Блок ввода. Пользователь вводит координаты вершин треугольника
a_x_cord = float(input("Введите координату x первой вершины: "))
a_y_cord = float(input("Введите координату y первой вершины: "))
b_x_cord = float(input("Введите координату x второй вершины: "))
b_y_cord = float(input("Введите координату y второй вершины: "))
c_x_cord = float(input("Введите координату x третьей вершины: "))
c_y_cord = float(input("Введите координату y третьей вершины: "))

# Назовем точку P
p_x_cord = float(input("Введите координаты x точки для проверки: "))
p_y_cord = float(input("Введите координаты y точки для проверки: "))

error = None # будем хранить ошибку и ответ в разных переменных
answer = '\n' 
eps = 1e-10 # зададим погрешность для сравнения чисел

# Проверка на правильность ввода
if int(a_x_cord) != a_x_cord or int(a_y_cord) != a_y_cord\
    or int(b_x_cord) != b_x_cord or int(b_y_cord) != b_y_cord\
        or int(c_x_cord) != c_x_cord or int(c_y_cord) != c_y_cord:
    error = "Ошибка! Введенные координаты должны быть целочисленными"
else:
    a_x_cord = int(a_x_cord)
    a_y_cord = int(a_y_cord)
    b_x_cord = int(b_x_cord)
    b_y_cord = int(b_y_cord)
    c_x_cord = int(c_x_cord)
    c_y_cord = int(c_y_cord)
    
# Проверка на совпадение точек
if error is None and (a_x_cord == b_x_cord and a_y_cord == b_y_cord)\
    or (a_x_cord == c_x_cord and a_y_cord == c_y_cord)\
        or (c_x_cord == b_x_cord and c_y_cord == b_y_cord):
            error = 'Ошибка! Такого треугольника не существует!'

# Проверка на неколлинеарность
# Узнаем координаты векторов ( сторон )
vec_AB_x = b_x_cord - a_x_cord
vec_AB_y = b_y_cord - a_y_cord
vec_CB_x = c_x_cord - b_x_cord
vec_CB_y = c_y_cord - b_y_cord
vec_CA_x = c_x_cord - a_x_cord
vec_CA_y = c_y_cord - a_y_cord

if error is None and ((vec_AB_x/vec_CB_x) == (vec_AB_y/vec_CB_y))\
    or ((vec_AB_x/vec_CA_x) == (vec_AB_y/vec_CA_y))\
        or ((vec_CA_x/vec_CB_x) == (vec_CA_y/vec_CB_y)):
            error = 'Ошибка! Такого треугольника не существует!'

if error is None:
    side_AB = ((b_x_cord - a_x_cord)**2 + (b_y_cord - a_y_cord)**2)**0.5
    side_CB = ((c_x_cord - b_x_cord)**2 + (c_y_cord - b_y_cord)**2)**0.5
    side_CA = ((c_x_cord - a_x_cord)**2 + (c_y_cord - a_y_cord)**2)**0.5
    
    answer += f"Стороны треугольника равны {side_AB:.5g}, {side_CA:.5g}, {side_CB:.5g}\n"
    
    # Узнаем максимальную, минимальную и третью строку
    if side_AB >= side_CB:
        if side_CB >= side_CA:
            min_side, avg_side, max_side = side_CA, side_CB, side_AB
        else:
            if side_AB >= side_CA:
                min_side, avg_side, max_side = side_CB, side_CA, side_AB
            else:
                min_side, avg_side, max_side = side_CB, side_AB, side_CA
    else:
        if side_CB >= side_CA:
            if side_AB >= side_CA:
                min_side, avg_side, max_side = side_CA, side_AB, side_CB
            else:
                min_side, avg_side, max_side = side_AB, side_CA, side_CB
        else:
            min_side, avg_side, max_side = side_AB, side_CB, side_CA
            
    # Узнаем высоту из большего угла
    p = (side_AB + side_CA + side_CB)/2
    s_triangle = (p*(p-side_CB)*(p-side_AB)*(p-side_CA))**0.5
    height = s_triangle*2/max_side
    
    answer += f'Высота из большего угла треугольника = {height:.5g}\n'
    
    # Проверим, является ли треугольник прямоугольным
    triangle_is_rectangular = (max_side**2 - (min_side**2 + avg_side**2)) < eps
    
    if triangle_is_rectangular:
        answer += f'Треугольник является прямоугольным\n'
    else:
        answer += f'Треугольник не является прямоугольным\n'
    
    # Проверим, находится ли точка внутри треугольника
    # Найдем площади треугольников BCP, ACP, ABP
    s_BCP = abs( (b_x_cord - p_x_cord)*(c_y_cord - p_y_cord)
                 - (c_x_cord - p_x_cord)*(b_y_cord - p_y_cord) ) / 2
    
    s_ACP = abs( (a_x_cord - p_x_cord)*(c_y_cord - p_y_cord)
                 - (c_x_cord - p_x_cord)*(a_y_cord - p_y_cord) ) / 2

    s_ABP = abs( (a_x_cord - p_x_cord)*(b_y_cord - p_y_cord)
                 - (b_x_cord - p_x_cord)*(a_y_cord - p_y_cord) ) / 2
    
    if abs(s_BCP + s_ACP + s_ABP - s_triangle) < eps:
        
        height_to_AB = s_ABP*2 / side_AB
        height_to_CB = s_BCP*2 / side_CB
        height_to_CA = s_ACP*2 / side_CA
        
        height_to_triangle = min(height_to_AB, height_to_CB, height_to_CA)
        
        answer += f'Точка ({p_x_cord:.5g}, {p_y_cord:.5g}) находится внутри треугольника\
            \nРасстояние до треугольника = {height_to_triangle:.5g}\n'
    else:
        answer += f'Точка ({p_x_cord:.5g}, {p_y_cord:.5g}) находится вне треугольника'
    
# Блок вывода
if error:
    print(error)
else:
    print(answer)
