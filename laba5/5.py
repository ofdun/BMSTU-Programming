
# y = 1/(4n-1)(4n+1)

step = int(input())
number_of_iterations = int(input())
eps = float(input())

print('-' * 41)
print('| № Итерации  |', ' '*5 + 't' + ' '*4, '|', ' '*5 + 's' + ' '*5 + '|')
# t = current; s = sum
s = 0
its = 0


for i in range(1, number_of_iterations+1):
    t = 1/((4*i-1)*(4*i+1))
    s += t
    
    if i % step == 0:
        print(f'| {i:^12.5g}|{t:^12.5g}|{s:^12.5g}|')
        
    its = i
    if t < eps:
        break

print('-' * 41)

print(f'Сумма бесконечного ряда - {s:.5g}, вычислена за {its} итераций.')