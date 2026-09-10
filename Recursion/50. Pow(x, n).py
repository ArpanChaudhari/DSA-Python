def power(x: float, n: int) -> float:
    if n == 0 or x == 1:
        return 1

    if n == 1:
        return x

    if n % 2 == 0:
        return power(x * x, n // 2)

    return x * power(x, n - 1)


def myPow(x: float, n: int) -> float:

    if n < 0:
        n = -1 * n
        ans = power(x, n)
        return 1 / ans

    return power(x, n)

x = 2.00000
n = 10
# n = -4
print(myPow(x, n))

'''
x = 2
n = 10

first main call -> x,n
n = 10  even -> power(x*x, n//2) -> power(4, 5)
second call -> x,n
n = 5  odd -> x * power(x, n-1) -> 4 * power(4, 4)
third call -> x,n
n = 4 even -> power(x*x, n//2) -> power(16, 2)
fourth call -> x,n
n = 2 even -> power(x*x, n//2) -> power(256, 1)
fifth call -> x,n
n = 1 -> return x -> return 256

backtracking:
fifth call returns 256
fourth call returns 256
third call returns 4 * 256 = 1024
second call returns 1024
first call returns 1024

TC - O(log n) deal with half of the problem in each recursive call
SC - O(log n) call stack space
'''

