from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if self.possible(bloomDay, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def possible(self, bloomDay: List[int], days: int, m, k):
        counter = 0
        bouPos = 0
        for day in bloomDay:
            if day <= days:
                counter += 1
            else:
                bouPos += counter // k
                counter = 0
        bouPos += counter // k

        if bouPos < m:
            return False
        else:
            return True


Solution = Solution()
bloomDay = [7,7,7,7,13,11,12,7]
m = 2
k = 3
print(Solution.minDays(bloomDay,m,k))