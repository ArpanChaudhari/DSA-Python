def divide(dividend: int, divisor: int) -> int:

    if dividend == -(2**31) and divisor == -1:
        return 2**31 - 1

    is_negative = (dividend < 0) ^ (divisor < 0)

    d = abs(dividend)
    n = abs(divisor)

    ans = 0

    while d >= n:
        shift = 0
        while d >= (n << (shift + 1)):
            shift += 1

        ans += 1 << shift
        d -= n << shift

    return -ans if is_negative else ans

dividend = 10
divisor = 3
result = divide(dividend, divisor)
print(result)  # Output: 3