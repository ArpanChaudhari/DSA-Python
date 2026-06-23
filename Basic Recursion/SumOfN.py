def sumOfNnumber(n):
    if n == 0:
        return 0
    return n + sumOfNnumber(n - 1)


print(sumOfNnumber(4))
