def lengthOfLastWord(s: str) -> int:
    n = len(s)
    count = 0

    for ch in range(n - 1, -1, -1):
        if s[ch] == " " and count != 0:
            return count
        if s[ch] != " ":
            count += 1

    return count

s = "Hello World"
print(lengthOfLastWord(s))