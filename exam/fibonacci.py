def recursive(n,obj={}):
    if n in {0,1}:
        return n
    if n not in obj:
        obj[n] = recursive(n-1,obj)+recursive(n-2,obj)
    return obj[n]
print(recursive(int(input())))
