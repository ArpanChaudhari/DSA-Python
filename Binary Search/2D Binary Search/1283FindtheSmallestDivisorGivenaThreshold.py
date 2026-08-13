from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if self.possible(nums, mid, threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def possible(self, nums: List[int], divisor: int, threshold: int) -> bool:
        sum = 0
        for num in nums:
            sum += math.ceil(num / divisor)

        if sum <= threshold:
            return True
        else:
            return False

nums = [1,2,5,9]
threshold = 6

Solution = Solution()

print(Solution.smallestDivisor(nums,threshold))