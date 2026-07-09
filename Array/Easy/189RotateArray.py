from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k % n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


Solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
