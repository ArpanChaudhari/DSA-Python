from typing import List


def missingInteger(nums: List[int]) -> int:
    prefix_sum = nums[0]
    i = 1
    while i < len(nums) and nums[i] == nums[i - 1] + 1:
        prefix_sum += nums[i]
        i += 1

    while prefix_sum in nums:
        prefix_sum += 1

    return prefix_sum

nums = [1,2,3,2,5]
print(missingInteger(nums))
