def maxvowelss(s: str, k: int) -> int:
    count = 0
    vowels = {"a", "e", "i", "o", "u"}

    for i in range(k):
        if s[i] in vowels:
            count += 1

    if count == k:
        return k

    max_count = count

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            count -= 1

        if s[i] in vowels:
            count += 1

        if count > max_count:
            max_count = count

        if max_count == k:
            return k

    return max_count


s = "weallloveyou"
k = 7 
print(maxvowelss(s,k))