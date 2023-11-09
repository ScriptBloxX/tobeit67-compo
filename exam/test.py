x = int(input())
y = int(input())
n = int(input())

y_set = y
table = {}
for set in range(x):
    table['set'+str(set)] = ''
    for i in range(y):
        if n > 0:
            n-=1
            y_set-=1
            table['set'+str(set)]+='*'
        elif n < 1 and y_set > 0:
            print(y_set,'y-set')
            y_set-=1
            table['set'+str(set)]+=' '
sortTable = sorted(table,reverse=True)
print('-'*(x+2))
for i in sortTable:
    if table[i] != '':
        stars = table[i]
        if len(stars) < x:
            for space in range(x-len(stars)):
                stars+=' '
        print('|'+stars+'|')
print('-'*(x+2))
print(f'There are {n} stars left.')
