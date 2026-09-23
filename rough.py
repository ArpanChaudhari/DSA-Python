def reverseDegree(s: str) -> int:
    Total_sum = 0
    for i, ch in enumerate(s):
        print(123 - ord(ch))
        Total_sum += ((123 - ord(ch)) * (i + 1))

    return Total_sum


s = "abc"
print(reverseDegree(s))