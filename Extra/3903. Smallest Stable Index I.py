from typing import List


def firstStableIndex(nums: list[int], k: int) -> int:

    # Solution 1 (TC- O(n^2), SC-O(1))
    '''
    for i in range(len(nums)):
        stable = max(nums[: i + 1]) - min(nums[i:])
        if stable <= k:  # need smallest index not smallest stable value
            return i

    return -1

    '''

    # Solution 2 (TC- O(n), SC-O(n))
    n = len(nums)
    prefix_max = [0] * n
    suffix_min = [0] * n

    prefix_max[0] = nums[0]

    for i in range(1,n):
        prefix_max[i] = max(prefix_max[i-1], nums[i])

    suffix_min[-1] = nums[-1]

    for i in range(n-2,-1,-1):
        suffix_min[i] = min(suffix_min[i+1], nums[i])

    for i in range(n):
        if prefix_max[i] - suffix_min[i] <= k:
            return i
        
    return -1


nums = [5,0,1,4]
k = 3
print(firstStableIndex(nums, k))  # Output: 2