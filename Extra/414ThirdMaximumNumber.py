from typing import List


def thirdMax( nums: List[int]) -> int:
    first = second = third = float("-inf")
    for i in nums:
        if i == first or i == second or i == third:
            continue

        if i > first:
            third = second
            second = first
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i

    return first if third == float("-inf") else third

nums = [3, 2, 1]
print(thirdMax(nums))  # Output: 1
