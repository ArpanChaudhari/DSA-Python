from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            current = nums[i]
            next_value = nums[(i + 1) % n]

            if current > next_value:
                count += 1

        return count <= 1


list = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.check(list))
