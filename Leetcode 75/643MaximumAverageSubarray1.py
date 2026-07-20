from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    window_sum = 0

    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    left = 0
    for right in range(k, len(nums)):
        window_sum = window_sum + nums[right] - nums[left]
        left += 1

        max_sum = max(max_sum, window_sum)

    return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))
