def longestPalindrome(s: str) -> str:
    n = len(s)
    max_length = best_left = best_right = 0
    for i in range(n):

        left, right = i, i

        while left >= 0 and right < n and s[left] == s[right]:

            length = right - left + 1

            if length > max_length:
                max_length = length
                best_left = left
                best_right = right

            left -= 1
            right += 1

        left, right = i, i + 1

        while left >= 0 and right < n and s[left] == s[right]:

            length = right - left + 1

            if length > max_length:
                max_length = length
                best_left = left
                best_right = right

            left -= 1
            right += 1

    return s[best_left : best_right + 1]

s = "babad"
print(longestPalindrome(s))