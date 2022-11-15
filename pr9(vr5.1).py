with open('/DimaChikunov/python/pr9/vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print(matrix)
m=len(matrix)
n=len(matrix[0])
a=matrix
for i in range(m):
    for j in range(n):
        a[i].sort()
print(str(a))
with open('/DimaChikunov/python/pr9/vivod3.txt', 'w', encoding='utf-8-sig') as f:
    f.write(str(a))
f.close()