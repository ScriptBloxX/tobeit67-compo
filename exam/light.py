n = int(input())

table = {}
for i in range(1,n+1):
    table[i] = ''

for i in range(1,n+1):
    for k in table:
        if k % i == 0:
            if table[k] == '':
                table[k] = 'blue'
            elif table[k] == 'blue':
                table[k] = 'orange'
            elif table[k] == 'orange':
                table[k] = ''
count = 0
for i in table:
    if table[i] != '':
        count += 1
print(count)
