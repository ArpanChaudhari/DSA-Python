from turtle import right
from typing import List


def compress(chars: List[str]) -> int:
    n = len(chars)

    if n == 1:
        return 1

    left = right = write = 0

    while left < n:
        right = left

        while right < n and chars[left] == chars[right]:
            right += 1

        count = right - left

        chars[write] = chars[left]
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

        left = right

    return write


nums = ["a", "a", "b", "b", "c", "c", "c"]
# nums = ["a", "b"]
result = compress(nums)
print(result)
print(nums[:result])
