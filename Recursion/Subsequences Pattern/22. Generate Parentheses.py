from typing import List


class Solution:
    def generate(self, current, open, close, n, result):
        if len(current) == n * 2:
            result.append(current)
            return

        if open < n:
            self.generate(current + "(", open + 1, close, n, result)

        if close < open:
            self.generate(current + ")", open, close + 1, n, result)

        return result

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        return self.generate("", 0, 0, n, result)

solution  = Solution()
n = 4
resilt = solution.generateParenthesis(n)
print(resilt)