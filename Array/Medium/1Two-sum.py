from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i,num in enumerate(nums):
            diff=target-num

            if diff in hashmap :
                return [hashmap[diff],i]
            
            hashmap[num]=i

sol=Solution()
nums = [2,7,11,15]
target = 9

print(sol.twoSum(nums,target))