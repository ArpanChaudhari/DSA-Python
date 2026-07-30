from typing import List
def upperBound(nums: List[int], x: int)-> int:
    n = len(nums)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > x:
            ans = mid
            high = mid - 1
        else :
            low = mid + 1

    return ans 

# nums= [3,5,8,15,19]
# x = 9
# nums = [1,2,2,3]
# x = 2
nums = [3, 4, 4, 7, 8, 10]
x = 8
print(upperBound(nums,x))