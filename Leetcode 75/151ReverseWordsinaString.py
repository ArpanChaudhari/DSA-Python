def reverseWords(s: str) -> str:

    S_list = s.split()
    n = len(S_list)

    left, right = 0, n - 1
    while left < right:

        S_list[left], S_list[right] = S_list[right], S_list[left]

        left += 1
        right -= 1

    return " ".join(S_list)

s = "the sky is blue"
print(reverseWords(s))