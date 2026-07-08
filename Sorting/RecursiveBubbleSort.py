from typing import List


def recursiveBubbleSort(nums: List[int], n: int):
    if n == 0:
        return
    Did_swap = False
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            Did_swap = True
    
    if Did_swap == False:
        return
    
    recursiveBubbleSort(nums, n - 1)

nums = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:")
print(nums)
recursiveBubbleSort(nums,len(nums))
print("After Using Bubble Sort:")
print(nums)

# Time complexity O(n2) in worst case and O(n) in best case