a = int(input())
b = int(input())
if a > b:
    for i in range(b, a + 1):
        if i % 2 != 0:
            print('Нечётное число между А и Б ', i)