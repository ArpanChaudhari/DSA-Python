class Solution:
    def isArmstrong(self, n):
        original=str(n)
        power=len(original)
        arm=0
        while n:
            digit=n%10
            arm+=digit**power
            n//=10
        
        if int(original)== arm :
            return True
        
        return False

sol = Solution()
n = int(input("Enter a numer:"))
print(sol.isArmstrong(n))