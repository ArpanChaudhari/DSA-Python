def minAddToMakeValid(s: str) -> int:
    open_count = ans = 0
    for br in s:
        if br == "(":
            open_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            else:
                ans += 1

    return open_count + ans

s = "())()(()"
print(minAddToMakeValid(s)) 