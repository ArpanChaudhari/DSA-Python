def isIsomorphic(s: str, t: str) -> bool:
    map1 = {}
    map2 = {}

    for s, t in zip(s, t):
        if s in map1 and map1[s] != t:
            return False

        if t in map2 and map2[t] != s:
            return False

        map1[s] = t
        map2[t] = s

    return True


s = "egg"
t = "add"
print(isIsomorphic(s,t))