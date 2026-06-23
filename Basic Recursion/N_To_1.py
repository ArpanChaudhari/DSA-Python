def nToOne(n):
    if(n==0):
        return
    print(n)
    nToOne(n-1)
nToOne(5)