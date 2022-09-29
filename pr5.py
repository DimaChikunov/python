s = input('Введите строку \n')
for a in s.split():
    if(a.startswith('а') or a.endswith('я')):
        print(a)
