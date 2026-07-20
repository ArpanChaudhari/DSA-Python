from typing import List


def maxSubArray(nums: List[int]) -> int:
    current_sum = 0
    max_sum = nums[0]

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))