from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Finds the minimum largest subarray sum possible for at most k partitions
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low) // 2
            partitions = self.count_partitions(nums, mid)

            if partitions <= k:  # try smaller max_sum
                high = mid - 1
            else:  # too many partitions
                low = mid + 1
        return low

    def count_partitions(self, nums: List[int], max_sum: int):
        # Counts how many partitions are needed for a given max_sum
        partitions = 1
        subarray_sum = 0

        for num in nums:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num

        return partitions

sol = Solution()
nums = [7,2,5,10,8]
k = 2
print(sol.splitArray(nums,k))