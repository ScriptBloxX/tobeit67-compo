x = int(input())
y = int(input())
n = int(input())
n_set = n
y_set = y
table = {}
for set in range(x):
    if y <= n_set:
        table['set'+str(set)] = ''
    for i in range(y):
        print('y->',y,'n_set->',n_set,'y_set',y_set)
        if n > 0:
            n-=1
            y_set-=1
            if y <= n_set:
                print('a')
                table['set'+str(set)]+='*'
            elif y >= n_set:
                print('b')
                if not 'set'+str(set) in table:
                    table['set'+str(set)] = ''
                table['set'+str(set)]+='|'+' '*(x-1)+'*|\n'
        elif n < 1 and y_set > 0:
            print(y_set,'y-set',set)
            if not 'set'+str(y_set) in table:
                print('c','set'+str(y_set))
                table['set'+str(y_set)] = ''
            table['set'+str(y_set)]+='|'+' '*(x)+'|'
            print('DEBuG:',table)
            y_set-=1
print(table)
sortTable = sorted(table,reverse=True)
print('-'*(x+2))
for i in sortTable:
    if table[i] != '':
        stars = table[i]
        if stars.count('*') < x:
            for space in range(x-stars.count('*')):
                stars+=' '
        if y <= n_set:
            print('|'+stars+'|')
        elif y >= n_set:
            # table['debug'] = stars[::-1]
            # print(table)
            print(stars[::-1][stars[::-1].find('|'):])
print('-'*(x+2))
if n>1:
    print(f'There are {n} stars left.')
else:
    print(f'There are {n} star left.')

