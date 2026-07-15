from typing import List


def sortColors(nums: List[int]) -> None:
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1


nums= [2,0,2,1,1,0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]