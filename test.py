'''Hello <i>Judge'''

def main():
    '''Main Function'''
    # Write your code here

    testCase = [[1,1,1,2],[3,4,5,3],[5,0,4,9],[20,2,5,10],[6,7,3,11],[0,6,8,12],[4,7,3,8],[5,1,4,8],[0,0,0,0],[5,3,6,7],[5,2,4,5]]

    for i in range(len(testCase)):
        units,prices = Get_UnitPrice(testCase[i][0],testCase[i][1],testCase[i][2],testCase[i][3])
        print(testCase[i])
        print(round(units),'ชิ้น')
        print(round(prices),'บาท')
    return

    hamburger_price = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # units,prices = Get_UnitPrice(hamburger_price, b, c, d)
    # print(round(units),'ชิ้น')
    # print(round(prices),'บาท')

def Get_UnitPrice(hamburger_price, b, c, d):
    if d < b or c < 1:
        return d, d * hamburger_price
    if b < 1:
        i = 0
        while i < c - 1:
            i += 1
        d = i * c
        price = 0
        return d, price
    if c > b and not b + c >= d:
        buy_burger = (d / c) * b
        price = buy_burger * hamburger_price
        d += buy_burger
        return d, price
    if b + c >= d and not b == 1 and not c == 1 and hamburger_price == 0:
        return b + c, (d - (b + c)) * hamburger_price
    if b + c >= d and not b == 1 and not c == 1 and not hamburger_price == 0:
        buy_p = d // b
        if b+c >= d:
            return b+c,b*hamburger_price
        free_burger = buy_p * c
        buy_burger = buy_p * b
        d = buy_burger + free_burger
        price = buy_burger * hamburger_price
        return d, price

    free_burger = (d // (b + c)) * c
    price = (d - free_burger) * hamburger_price
    return d, price

main()
