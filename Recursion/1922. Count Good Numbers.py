class Solution:
    MOD = 10**9 + 7

    def power(self, x, n):
        if n == 0:
            return 1

        # approach 1
        '''
        half = self.power(x, n // 2)

        if n % 2 == 0:
            return (half * half) % self.MOD
        else:
            return (x * half * half) % self.MOD
        '''

        # approach 2
        if n % 2 == 0:
            return self.power((x * x) % self.MOD, n // 2)
        else:
            return (x * self.power(x, n-1)) % self.MOD

    def countGoodNumbers(self, n: int) -> int:
        pair = n // 2

        ans = self.power(20, pair)

        if n % 2 == 1:
            return (5 * ans) % self.MOD

        return ans

solution = Solution()
n = 50
result = solution.countGoodNumbers(n)
print(result)  # Output: 564908303