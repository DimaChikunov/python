#вариант 3: номер 1
print('НОМЕР_1')

import math
a = int(input('Введите первый катет a: '))
b = int(input('Введите второй катет катет b: '))
a1 = int(input('Введите первый катет a1: '))
b1 = int(input('Введите второй катет b1: '))
def tr1(a,b):
    c = a**2 + b**2
    n = math.sqrt(c)
    return n
def tr2(a,b):
    c = a**2 + b**2
    n = math.sqrt(c)
    return n
if tr1(a,b) > tr2(a1,b1):
    print('первая гипотенуза больше')
else:
    print('вторая гипотенуза больше')

#номер_2
print('НОМЕР_2')
def sort(s):
    return (sorted(s))
    return s[1]
s = str(input('Введите строку'))
print(sorted(s))