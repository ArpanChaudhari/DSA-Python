class Solution:
    def findRangeXOR(self, l, r):
        return self.XOR(l - 1) ^ self.XOR(r)

    def XOR(self, n):
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        if n % 4 == 3:
            return 0
        if n % 4 == 0:
            return n


solution = Solution()
l = 3
r = 7
print(solution.findRangeXOR(3, 7))
