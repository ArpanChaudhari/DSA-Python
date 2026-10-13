from typing import List


def maxAlternatingSum(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        nums[i] = nums[i] ** 2

    nums.sort()

    score = 0
    left = 0
    right = n - 1

    while right >= (n // 2):
        score += nums[right]
        right -= 1

    while left < (n // 2):
        score -= nums[left]
        left += 1

    return score

nums = [1,-1,2,-2,3,-3]
print(maxAlternatingSum(nums))  