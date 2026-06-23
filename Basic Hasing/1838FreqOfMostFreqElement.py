from typing import List


def maxFrequency(nums: List[int], k: int) -> int:
    left = 0
    nums.sort()
    sum = 0
    freq = 0
    for right in range(len(nums)):
        sum += nums[right]

        while (nums[right] * (right - left + 1) - sum) > k:
            sum -= nums[left]
            left += 1

        freq = max(freq, right - left + 1)
    return freq


nums = [1, 4, 8, 13]
k = 5

print(maxFrequency(nums, k))
