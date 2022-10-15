#вариант 1: номер 1
print('НОМЕР_1')

n = int(input('Введите длину массива: '))
a = []
for i in range(n):
    print('Введите',i,'элемент: ')
    a.append((int(input())))
print('Исходный массив: ',a)
mx = 0
for i in a:
    if i > mx:
        mx = i
print('Максимальный элемент массива: ', mx)
a.reverse()
print('Перевёрнутый массив', a)

#номер_2
print('НОМЕР_2')
from random import random
a = []
for i in range (5):
    a.append(int(random()*5))
print (a)
b= sum(a)/len(a)
for i in range(len(a)):
    if a[i]==0:
        a[i]=b
print(b)
print (a)

