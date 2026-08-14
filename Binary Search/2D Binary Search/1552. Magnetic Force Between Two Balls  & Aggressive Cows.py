from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Aggressive cows
        position.sort()
        low = 1
        high = (position[-1] - position[0]) // (m - 1)

        while low <= high:
            mid = low + (high - low) // 2

            if self.canWePlace(position, m, mid):
                low = mid + 1
            else:
                high = mid - 1

        return high

    def canWePlace(self, position: List[int], m: int, force: int):
        countBall = 1
        last = position[0]

        for i in range(1, len(position)):
            if position[i] - last >= force:
                countBall += 1
                last = position[i]

            if countBall >= m:
                return True

        return False

position = [79,74,57,22]
m = 4

sol = Solution()
print(sol.maxDistance(position,m))
