from typing import List


class Solution:
    def findPages(self, nums: List[int], m: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if self.countStudent(nums, mid) <= m:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def countStudent(self, nums, pages):
        stdcount = 1
        currentPage = 0

        for i in range(len(nums)):
            if currentPage + nums[i] <= pages:
                currentPage += nums[i]
            else:
                stdcount += 1
                currentPage = nums[i]

        return stdcount

nums = [12, 34, 67, 90]
m=2
sol = Solution()
print(sol.findPages(nums,m))