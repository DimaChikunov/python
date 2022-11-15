with open('/DimaChikunov/python/pr9/vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print(matrix)
m=len(matrix)
n=len(matrix[0])
a=matrix
for i in range(m):
    if i%2==0:
        minimum = min(a[i])
        print('Минимум строки', (str(i)),'равен', (str(minimum)))
        with open('/DimaChikunov/python/pr9/vivod1.txt', 'a+', encoding='utf-8-sig') as f:
            f.write('min элемент чётной строки  ')
            f.write(str(i))
            f.write('\n')
            f.write('равен  ')
            f.write(str(minimum))
            f.write('\n')
f.close()