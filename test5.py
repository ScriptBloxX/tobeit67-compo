otp_list = []
while True:
    n=input()
    if n=='0':
        break
    otp_list.append(n)

def findkey(n):
    i = [key for key, value in n.items() if value > 1]
    v = [n[key] for key in i]
    return len(i),sum([length for length in v])

def cd(n):
    s = set()
    result = 0
    if len(n)==4:
        for i in n:
            if i in s:
                result += 1
            else:
                s.add(i)
    if len(n)==6 or len(n)==8:
        result={}
        for i in n:
            if not i in s:
                s.add(i)
                result[i] = 1
            elif i in s:
                result[i] += 1
        return findkey(result)

    duplicate_count = {}

    for i in n:
        if n.count(i) > 1 and i not in duplicate_count:
            duplicate_count[i] = n.count(i)
    duplicate_lengths = sum([length for length in duplicate_count.values()])

    return result, duplicate_lengths

def otp_check(n):

    r1,r2 = cd(n)
    # print(len(n),r1,r2)

    if len(n) == 4 and r1==1 and r2==2:
        return True
    elif len(n) == 6 and (r1==2 and r2==4) or len(n) == 6 and (r1==1 and r2==3):
        return True
    elif len(n) == 8 and (r1==3 and r2==6) or len(n) == 8 and (r1==2 and r2==6):
        return True
    return False
    
for otp in otp_list:
    if otp_check(otp):
        print('Valid')
    else:
        print('Invalid')
