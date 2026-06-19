class Solution:
    def fib(self, n: int) -> int:
        if(n<=1):
            return n

        last=self.fib(n-1)
        slast=self.fib(n-2)
        return last+slast
    
n=6
sol=Solution()
print(sol.fib(n))