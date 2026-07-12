from typing import List


def longestSubarray(nums: List[int], k: int) -> int:
    prefix_sum = 0
    maxi = 0
    n = len(nums)
    prefix_map: dict[int, int] = {}

    for i in range(n):
        prefix_sum += nums[i]

        if prefix_sum == k:
            maxi = max(maxi, i + 1)
        
        remaining = prefix_sum - k
        
        if remaining in prefix_map:
                length = i - prefix_map[remaining]
                maxi = max(maxi, length)
        
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return maxi


nums = [2, -1, 1, 2]
k = 3
print(longestSubarray(nums, k))
