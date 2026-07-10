
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
        maximum=0
        left=0
        for right in range(len(nums)):
            if nums[right] == 1:
                maximum=max(maximum,(right-left)+1)
            else:
                left=right+1
        return  maximum

nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))