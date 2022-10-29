print('НОМЕР_1')
m=int(input('Введите количество строк: '))
n=int(input('Введите количество столбцов: '))
a=[]
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
print('Исходный массив: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end= ' ')
    print()
for i in range(0, m, 2):
    minimum = min(a[i])
    print('Минимум строки %d равен %d' % (i, minimum))

print('НОМЕР_2')
m=int(input('Введите количество строк: '))
n=int(input('Введите количество столбцов: '))
maximum = float('-inf')
minimal = float('inf')
a=[]
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
print('Исходный массив: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end= ' ')
    print()
for i in range(m):
        for j in range(n):
                if a[i][j] > maximum:
                        maximum = a[i][j]
                if a[i][j] < minimal:
                        minimal = a[i][j]
print("Максимальное число: ", maximum,"Минимальное число: ", minimal)
for i in range(m):
        for j in range(n):
                if a[i][j] == maximum:
                        a[i][j] = minimal
                elif a[i][j] == minimal:
                        a[i][j] = maximum
print('Полученный массив: ')
for i in range(m):
        for j in range(n):
                print(a[i][j], end=' ')
        print()