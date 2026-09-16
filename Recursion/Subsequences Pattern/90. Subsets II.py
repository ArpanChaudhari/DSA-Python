from typing import List


class Solution:
    def printSubsets(self, nums, i, ans, result):
        if i == len(nums):
            result.append(ans.copy())
            return

        ans.append(nums[i])
        self.printSubsets(nums, i + 1, ans, result)

        ans.pop()

        # SKIPPING DUPLICATE VALUES
        idx = i + 1
        while idx < len(nums) and nums[i] == nums[idx]:
            idx += 1

        self.printSubsets(nums, idx, ans, result)

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # WE NEED TO COMBINED DUPLICATE VALUE TO SKIP
        nums.sort()
        result = []
        ans = []

        self.printSubsets(nums, 0, ans, result)

        return result

solution = Solution()
nums = [1,2,2]
result = solution.subsetsWithDup(nums)

print(result)