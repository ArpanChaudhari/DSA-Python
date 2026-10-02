class Solution:
    def addDigits(self, num):
        def solve(num):
            if num == 0:
                return 0

            return num % 10 + solve(num // 10)

        if num < 10:
            return num
        
        digit_sum = solve(num)

        if digit_sum < 10:
            return digit_sum
        
        return self.addDigits(digit_sum)

n = 3894
print(Solution().addDigits(n))