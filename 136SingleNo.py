from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for i in nums:
            xor=xor^i
        return xor
    
list=[2,2,1]
solution = Solution()   
print(solution.singleNumber(list))