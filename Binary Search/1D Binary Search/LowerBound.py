from typing import List
def lowerBound(nums: List[int], x: int)-> int:
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high :
        mid  = (low + high) // 2

        if nums[mid] >= x:
            ans = mid
            high = mid - 1
        else :
            low = mid + 1

    return ans

nums= [3,5,8,15,19]
x = 9
print(lowerBound(nums,x))