def addUp(n):
    if n == 0:
        return 0
    else:
        return n + addUp(n-1)
    
print(addUp(5))
    