from typing import List


class Solution:
    def find_floor(self, nums, x):
        n = len(nums) - 1
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= x:
                ans = nums[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def find_ceil(self, nums, x):
        n = len(nums) - 1
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <=  x:
                ans = nums[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def get_floor_and_ceil(self, nums: List[int], x: int) -> int:
        floor = self.find_floor(nums, x)
        ceil = self.find_ceil(nums, x)
        return floor, ceil


nums = [3, 4, 4, 7, 8, 10]
x = 8
sol = Solution()
f, c = sol.get_floor_and_ceil(nums, x)
print(f, c)
