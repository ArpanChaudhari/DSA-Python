def isPowerOfThree(n: int) -> bool:
    if n > 0 and 3**19 % n == 0:
        return True

    return False

n = 27
print(isPowerOfThree(n))