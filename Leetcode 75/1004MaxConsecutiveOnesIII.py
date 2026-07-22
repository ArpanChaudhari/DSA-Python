from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    left = 0
    window_size = 0
    for i in range(n):
        if nums[i] == 0:
            count += 1

        while count > k:
            if nums[left] == 0:
                count -= 1
            left += 1

        window_size = max(window_size, i - left + 1)

    return window_size


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums,k))