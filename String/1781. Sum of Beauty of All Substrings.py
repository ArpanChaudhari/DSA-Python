def beautySum(s: str) -> int:
    n = len(s)
    total = 0
    for left in range(n):
        hashmap = {}
        for right in range(left, n):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            total += max(hashmap.values()) - min(hashmap.values())

    return total

s = "abaacc"
print(beautySum(s))