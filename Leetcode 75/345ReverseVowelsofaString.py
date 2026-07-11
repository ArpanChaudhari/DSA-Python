def reverseVowels(s: str) -> str: # type: ignore
    temp = list(s)
    Vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    left = 0
    right = len(temp) - 1
    while left < right:

        while left < right and temp[left] not in Vowels:
            left += 1

        while left < right and temp[right] not in Vowels:
            right -= 1

        temp[left], temp[right] = temp[right], temp[left]
        left += 1
        right -= 1

    return "".join(temp)


str = "IceCreAm"
result = reverseVowels(str)
print(result)