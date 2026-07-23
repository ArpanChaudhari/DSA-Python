from typing import List


def longestSubarray(nums: List[int]) -> int:
    zero_count = 0
    max_length = 0
    left = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, i - left + 1)

    return max_length - 1

nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))