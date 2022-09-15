import math
x = float(input('Введите переменную x: '))
y = float(input('Введите переменную y: '))
z = float(input('Введите переменную z: '))
s = ((y ** (x + 1)) / ((((math.pow(math.fabs(y - 2) , 1 / 3))) + 3)) + ((x + y / 2)) / (2 * (math.fabs((x + y)))) * ((x + 1) ** (-1 / math.sin(x))))
print("s = {0:.2f}".format(s))
