#вариант 7: номер 1
print('НОМЕР_1')
import math

x = float(input('x : '))
y = float(input('y : '))
z = float(input('z : '))
t = float(input('t : '))
d = math.sqrt(x * x + y * y)
def Square1(x, y):
    return  x * y * 0.5


def Square2(d, z, t):
    p = (z + t + d) / 2
    return math.sqrt(p * (p - z) * (p - t) * (p - d))

print('Диагональ 4-х угольника равна: ',d)
print('Площадь_1: ',Square1(x, y))
print('Площадь_2: ',Square2(d, z, t))

#номер_2
print('НОМЕР_2')
def d(n):
    a = ""
    while n != 0:
        a = str(n%8) + a
        n //= 8
    return "{0:0>10}".format(a)
b = int(input('Введите число: '))
print(d(b))