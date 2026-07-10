from typing import List


def linearSearch(nums: List[int], target: int) -> int:
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == target:
            return i
        i += 1
    return -1


nums = [2, 3, 4, 5, 3]
target = 3
print(linearSearch(nums, target))
