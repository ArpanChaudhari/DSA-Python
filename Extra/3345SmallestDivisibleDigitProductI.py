class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n,n+11):
            if self.digitProduct(num) % t == 0:
                return num
    
    def digitProduct(self, n: int) -> int:
        product = 1
        while n > 0:
            digit = n % 10
            product *= digit
            n //= 10
        
        return product

Solution = Solution()

n = 15
t = 3
print(Solution.smallestNumber(n,t))