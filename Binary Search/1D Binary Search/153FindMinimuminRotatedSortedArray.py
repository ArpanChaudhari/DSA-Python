from typing import List


def findMin(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]


nums = [3, 4, 5, 1, 2]
print(findMin(nums))