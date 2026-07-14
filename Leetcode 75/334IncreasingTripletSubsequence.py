from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    n = len(nums)

    if n < 3:
        return False

    first = second = float("inf")

    for i in range(0, n):
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] <= second:
            second = nums[i]
        else:
            return True

    return False

nums = [1, 2, 3, 4, 5]
print(increasingTriplet(nums))  # Output: True
