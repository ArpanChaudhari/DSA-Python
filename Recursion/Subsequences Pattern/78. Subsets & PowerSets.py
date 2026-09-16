from typing import List


class Solution:
    def printSubsets(self, nums, i, ans, result):
        if i == len(nums):
            result.append(ans.copy())
            return

        ans.append(nums[i])
        self.printSubsets(nums, i + 1, ans, result)

        ans.pop()
        self.printSubsets(nums, i + 1, ans, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        ans = []

        self.printSubsets(nums, 0, ans, result)

        return result

solution = Solution()
nums = [1,2,3]
result = solution.subsets(nums)

print(result)