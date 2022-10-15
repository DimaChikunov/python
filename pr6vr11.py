    #вариант 11: номер 1
print('НОМЕР_1')
from random import random
a = []
for i in range (10):
    a.append(int(random()*25))
print (a)
mx=0
for i in a:
    if i > mx and i % 2 == 0:
        mx = i
print('Максимальный чётный элемент массива: ', mx)

    #номер_2
print('НОМЕР_2')
from random import random
a = []
for i in range (10):
    a.append(int(random()*15))
print (a)
b = []
for i in a:
    if i % 2 == 0 and i < 10 :
        b.append(i)
if len(b) == 0:
    print("Чисел по заданному условию нет.")
else:
    b.sort()
    print(b)