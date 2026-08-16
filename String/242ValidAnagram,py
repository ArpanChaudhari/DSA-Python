def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    n = len(s)
    hashmap1 = {}
    hashmap2 = {}

    for ch in range(n):
        hashmap1[s[ch]] = hashmap1.get(s[ch], 0) + 1
        hashmap2[t[ch]] = hashmap2.get(t[ch], 0) + 1

    return hashmap1 == hashmap2

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
