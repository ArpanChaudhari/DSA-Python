def LCM(n1,n2):
    x = n1 
    y = n2

    while y:
        x, y = y, x % y
    
    gcd = x

    return abs(n1 * n2) // gcd

n1 = 6
n2 = 4

print(LCM(n1,n2))