from typing import List


def singleNumberII(nums: List[int]) -> int:
    # Solution 1
    # ans = 0
    # n = len(nums)

    # for bitIndex in range(32):
    #     count = 0

    #     for i in range(n):

    #         if (nums[i] & (1 << bitIndex)):
    #             count += 1

    #     if count % 3 == 1:
    #         ans = ans | (1 << bitIndex)

    # return ans

    # time complexity = O(N X 32)

    # solution 2

    # nums.sort()
    # n = len(nums)

    # i = 1
    # while i < n :
    #     if nums[i] != nums[i - 1]:
    #         return nums[i - 1]
    #     i = i+3
    # return nums[n-1]
    
    #  time complexity = O(N X log N) + O(N/3) --> O(N log N) 
    # if nums size is 2^32 ->  2^32 X log 2^32  = 2^32 X 32 == solution 1 complexity but there is no possobility that array size is 2^32 so, this is optimal

    # Solution 3

    one = 0
    two = 0

    for num in nums:
        one = (one ^ num) & ~(two)
        two = (two ^ num) & ~(one)

    return one
    
    # time complexoity = O(N)

nums = [2, 2, 2, 1, 1, 1, 6, 4, 4, 4]
print(singleNumberII(nums))
