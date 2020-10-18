def myFab(n):
    newlist = []
    a,b = 0,1
    while a < n :
        newlist.append(a)
        a,b = b,a+b
    return newlist

print(myFab(100))

