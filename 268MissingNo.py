from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=(n*(n+1))//2
        for i in nums:
            sum-=i
        
        return sum
    
list=[0,1,3,4,5,6,7,8,9]
sol=Solution()
print(sol.missingNumber(list))