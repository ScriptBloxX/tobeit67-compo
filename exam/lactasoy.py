a = int(input()) #ราคา
b = int(input()) #จำนวนหลอดที่ต้องใช้
c = int(input()) #จำนวนราคาที่ลดลงต่อหลอดที่ใช้
d = int(input()) #จำนวนที่ต้องการ

soy_price = 0
discount = 0
l = 0

if b <= 0:
    soy_price = a*d
else:
    if c>a:
        c=a
    discount = (d//b)*c
    soy_price = (a*d)
    for i in range(d//b):
        soy_price-=a
    soy_price += discount

    if d%b == 0:
        soy_price+=2
        
print(soy_price)
