def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    return (n & n - 1) == 0 and (n & 0x55555555) != 0
    """
    0x55 -> 01010101 -> 
    4 -> 00000100
    0x55 & 4 -> 00000100
    for 32 bitmask -> 0x55555555 -> 01010101010101010101010101010101
    """

n = 256
print(isPowerOfFour(n))