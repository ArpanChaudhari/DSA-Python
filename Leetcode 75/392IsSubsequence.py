def isSubsequence(s: str, t: str) -> bool:
    n = len(s)
    left = 0
    for right in t:
        if left == n:
            break

        if s[left] == right:
            left += 1

    return left == len(s)

s= "abc"
t = "apbqcr"

print(isSubsequence(s, t))
