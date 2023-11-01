a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = float(input()) # teach f% per day
g = int(input()) # day

Ichika = 0 
Nino = 0
Miku = 0
Yotsuba = 0 
Itsuki = 0

# all_teach = 0
pass_count = 0

for i in range(g):
    Ichika+= (f/100)*a
    Nino +=(f/100)*b
    Miku +=(f/100)*c
    Yotsuba +=(f/100)*d
    print((f/100)*c,'<- Yotsuba learn curve [times]->',i,'days','Stack ->',Yotsuba)
    Itsuki +=(f/100)*e
    # all_teach += f

def sc(score):
    if score > 60:
        global pass_count
        pass_count+=1
        print('↙️ is pass with',(score),'learning from',60)
        return 'Pass'
    else:
        print('↙️ is fail with',(score),'learning from',60)
        return 'Fail'
    
# print(Ichika,Nino,Miku,Yotsuba,Itsuki,f)

print('Ichika :',sc(Ichika))
print('Nino :',sc(Nino))
print('Miku :',sc(Miku))
print('Yotsuba :',sc(Yotsuba))
print('Itsuki :',sc(Itsuki))
if pass_count < 3:
    print('Futaro Outtt!!!')
