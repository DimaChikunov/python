with open('/DimaChikunov/python/pr9/vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print(matrix)
m=len(matrix)
n=len(matrix[0])
a=matrix
for i in range(m):
    for j in range(n):
        a[i][j] = int(a[i][j])
for i in range(m):
    for j in range(n):
        if a[i][j] % 2 == 1:
            a[i][j] = 1
        elif a[i][j] % 2 == 0:
            a[i][j] = 0
print(str(a))
with open('/DimaChikunov/python/pr9/vivod4.txt', 'w', encoding='utf-8-sig') as f:
    f.write(str(a))
f.close()