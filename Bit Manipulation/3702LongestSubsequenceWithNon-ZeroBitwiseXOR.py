from typing import List


def longestSubsequence(nums: List[int]) -> int:
    xor = 0

    for num in nums:
        xor ^= num

    if xor != 0:
        return len(nums)

    for num in nums:
        if num != 0:
            return len(nums) - 1

    return 0


nums = [1,2,3]
print(longestSubsequence(nums))