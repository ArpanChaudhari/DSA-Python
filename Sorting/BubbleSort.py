from typing import List


def BubbleSort(nums: List[int]):  # Compare adjacent elements and swap them if arr[j] > arr[j+1].

    for i in range(len(nums) - 1, -1, -1):

        for j in range(i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


nums = [1, 5, 3, 9, 6]
print("Before Using Bubble Sort:")
print(nums)
BubbleSort(nums)
print("After Using Bubble Sort:")
print(nums)
