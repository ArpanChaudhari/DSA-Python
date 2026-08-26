def shortestBeautifulSubstring(s: str, k: int) -> str:
    best_length = len(s) + 1
    best_left = 0
    best_right = 0
    count = 0

    left = 0
    right = 0
    while right < len(s):

        if s[right] == "1":
            count += 1

        while count > k:
            if s[left] == "1":
                count -= 1
            left += 1

        if count == k:
            while s[left] == "0":
                left += 1

            current_length = right - left + 1

            if current_length < best_length:
                best_length = current_length
                best_left = left
                best_right = right

            elif current_length == best_length:
                
                # Check for lexicographically smaller
                if s[left : right + 1] < s[best_left : best_right + 1]:
                    best_left = left
                    best_right = right

        right += 1

    if best_length == len(s) + 1:
        return ""

    return s[best_left : best_right + 1]


s = "100011001"
k = 3

print(shortestBeautifulSubstring(s,k))