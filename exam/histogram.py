import statistics
def chart(n):
    checkList = []
    table = {}
    for i in n:
      if i not in checkList and i.isalpha():
        checkList.append(i)
        table[i] = n.count(i)
    sort_table = dict(sorted(table.items(), key=lambda x: (x[0], x[0])))
   
    values = list(sort_table.values())
    num=max(values)+1
    for i in range(sort_table[max(sort_table,key=sort_table.get)]):
        num-=1

        countList = []
        r = ''
        for i in sort_table:
           countList.append(sort_table[i])
        r = ''.join('^ ' if v >= num else '  ' for v in countList)
        print(str(num).zfill(3)+'|',r)
    r1 = ''
    for i in sort_table:
       r1+=f'{i} '
    print('>>>>',r1)
    print('MAX =',"{:.2f}".format(max(values))+',','MIN =',"{:.2f}".format(min(values))+',','AVG =',"{:.2f}".format(sum(values)/len(values))+',','S.D. =',"{:.2f}".format(statistics.stdev(values)))

chart(input())
