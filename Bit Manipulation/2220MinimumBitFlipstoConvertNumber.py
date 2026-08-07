def minBitFlips(start: int, goal: int) -> int:
    ans = start ^ goal
    count = 0
    while ans:
        ans = ans & (ans - 1)
        count += 1

    return count

a = 5
b = 9
print(minBitFlips(a,b))