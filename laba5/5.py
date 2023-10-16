# Автор: Калашников Елисей
# Группа: ИУ7-15Б
# Вариант 17
# Назначение программы: вычисление ряда 1/((4n-1)(4n+1))
# С заданной точностью и шагов

number_of_iterations = int(input('Введите количество итераций: '))
step = int(input('Введите шаг: '))
eps = float(input('Введите точность: '))

error = ''

if number_of_iterations <= 0 or step <= 0 or eps < 0:
    error = 'Ошибка! Введенные данные должны быть положительными'
    
if not error:

    offset = 41

    print('-' * offset)
    print('| № Итерации  |     t      |      s     |')
    print('-' * offset)
    # t = current; s = sum
    sum_ = 0
    its = 0
    resulted = False


    for i in range(1, number_of_iterations+1):
        current = 1/((4*i-1)*(4*i+1))
        sum_ += current
        
        if (i + step - 1) % step == 0:
            print(f'| {i:^12.5g}|{current:^12.5g}|{sum_:^12.5g}|')
            
        its = i
        if current < eps:
            resulted = True
            break
    else:
        print('-' * offset)
        print(f'Сумму ряда с точностью {eps} невозможно вычислить\
за заданное количество итераций')
        
    if resulted is True:
        print('-' * offset)
        print(f'Сумма бесконечного ряда - {sum_:.5g}, вычислена за {its} итераций.')
else:
    print(error)