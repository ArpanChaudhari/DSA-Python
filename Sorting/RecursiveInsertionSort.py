from typing import List


def recursiveInsertionSort(nums: List[int], i: int):
    if i == len(nums):
        return
    j = i
    while j > 0 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j-=1
    recursiveInsertionSort(nums, i + 1)


nums = [13, 46, 24, 52, 20, 9]
print("Before Using Insertion Sort:")
print(nums)
recursiveInsertionSort(nums,1)
print("After Using Insertion Sort:")
print(nums)

# Time complexity O(n2) in worst case and best case