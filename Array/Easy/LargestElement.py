from typing import List


def largest(nums: List[int]) -> int:
    max = float("-inf")

    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

    return max


nums = [1, 4, 5, 2, 6, 10]
print(largest(nums))
