from typing import List


class Solution:
    def generate(self, current, prev_zero, n, result):
        if len(current) == n:
            result.append(current)
            return

        if prev_zero:
            self.generate(current + "1", False, n, result)
        else:
            self.generate(current + "0", True, n, result)

            self.generate(current + "1", False, n, result)

        return result

    def validStrings(self, n: int) -> List[str]:
        # 0 -> 1
        # 1 -> 0,1
        curr = ""
        result = []

        return self.generate(curr, False, n, result)

solution = Solution()
n = 3
result = solution.validStrings(n)
print(result)