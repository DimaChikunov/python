#вариант 5: номер 1
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

print('полученный массив: ')
for i in range(m):
    for j in range(n):
        a[i].sort()
        print(a[i][j],end= ' ')
    print()

print('НОМЕР_2')
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
for i in range(m):
    for j in range(n):
        if a[i][j] % 2 == 1:
            a[i][j] = 1
        elif a[i][j] % 2 == 0:
            a[i][j] = 0
print('полученный массив: ')
for i in range(m):
    for j in range(n):
        print(a[i][j],end= ' ')
    print()