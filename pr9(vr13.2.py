with open('/DimaChikunov/python/pr9/vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print(matrix)
m=len(matrix)
n=len(matrix[0])
a=matrix
for i in range(m):
    for j in range(n):
        a[i][j]=int(a[i][j])
maximum = float('-inf')
minimal = float('inf')
for i in range(m):
        for j in range(n):
                if a[i][j] > maximum:
                        maximum = a[i][j]
                if a[i][j] < minimal:
                        minimal = a[i][j]
print("Максимальное число: ", (str(maximum)),"Минимальное число: ", (str(minimal)))
for i in range(m):
        for j in range(n):
                if a[i][j] == maximum:
                        a[i][j] = minimal
                elif a[i][j] == minimal:
                        a[i][j] = maximum
print(str(a))
with open('/DimaChikunov/python/pr9/vivod2.txt', 'w', encoding='utf-8-sig') as f:
    f.write(str(a))
f.close()