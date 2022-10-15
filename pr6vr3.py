    #вариант 3: номер 1
print('НОМЕР_1')
s = 0
from random import random
a = []
for i in range (5):
    a.append(int(random()*10))
print (a)
for i in range(5):
    if i % 2 ==0:
        s = a[i]+s
print('Сумма = ', s)

    #номер 2
print('НОМЕР_2')
from random import random
a = []
for i in range (8):
    a.append(int(random()*25))
print (a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i]*2
print(a)