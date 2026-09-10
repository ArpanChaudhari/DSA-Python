def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    return (n & n - 1) == 0  # 1-> 001 & 0-> 000 = 000 == 0
    # 16-> 10000 & 01111 = 00000 == 0

n = 16
print(isPowerOfTwo(n))
