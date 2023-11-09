x = int(input())
y = int(input())
n = int(input())

table = {}
resultTable = {}
for i in range(x):
    table['X'+str(i)] = []
    for i_y in range(y):
        table['X'+str(i)].append({'Y'+str(i_y):'X'})

for i in table:
    print(table[i])
    for dict_i in table[i]:
        for k,v in dict_i.items():
            print(v)
            if v == 'X' and n > 0:
                n-=1
                dict_i[k] = '*'

wait_for_print = ''
print('-'*(x+2))
for i in table:
    print(table[i],'debug')
    for dict in table[i]:
        for k,v in dict.items():
            wait_for_print+=f'{v}'
print(wait_for_print)
print('-'*(x+2))
if n>1:
    print(f'There are {n} stars left.')
else:
    print(f'There are {n} star left.')

