from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = low + (high - low) // 2

            if self.possible(weights, mid, days):
                high = mid - 1
            else:
                low = mid + 1

        return low

    def possible(self, weights: List[int], capacity, days: int) -> bool:
        day_needed = 1
        current_load = 0
        for w in weights:
            current_load += w
            if current_load > capacity:
                day_needed += 1
                current_load = w

        return day_needed <= days


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
Solution = Solution()
print(Solution.shipWithinDays(weights,days))
