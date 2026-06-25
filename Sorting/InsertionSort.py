from typing import List
def InsertionSort(nums:List[int]):
    for i in range(1,len(nums)):
        j=i
        while j>0 and nums[j-1]>nums[j]:
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j-=1

nums = [1, 5, 3, 9, 6]
print("Before Using Insertion Sort:")
print(nums)
InsertionSort(nums)
print("After Using Insertion Sort:")
print(nums)