from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        # left part sorted
        if nums[low] <= nums[mid]:

            # Target lies in left half
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right part sorted
        else:

            # Target lies in right half
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

nums = [6,7,1,2,3,4,5]
target = 6
print(search(nums,target))