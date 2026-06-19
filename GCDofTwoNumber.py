class Solution:
    def GCD(self, n1, n2):
        if n1==0:
            return n2
        if n2==0:
            return n1
        
        if n1>n2:
            return self.GCD(n1%n2,n2)
        else:
            return self.GCD(n1,n2%n1)
        
n1=4        
n2=6
sol=Solution()
print(sol.GCD(n1,n2))