from typing import List


def pivotIndex(nums: List[int]) -> int:
    n = len(nums)
    total_sum = sum(nums)

    left_sum = 0
    for i in range(n):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]

    return -1


nums = [1,7,3,6,5,6]
print(pivotIndex(nums))