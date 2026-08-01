from typing import List
def findPeakElement(nums: List[int]) -> int:
    low, high = 0 , len(nums)

    while low < high:
        mid = low + (high - low) // 2

        if nums[mid] > nums[mid+1]:
            high = mid
        else :
            low = mid + 1

    return low

# nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))