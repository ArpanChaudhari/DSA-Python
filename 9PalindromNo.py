class Solution:
    def isPalindrome(self, x: int) -> bool:
        # method 1
        # return x>=0 and str(x) == str(x)[::-1]


        # method 2
        # if x < 0:
        #     return False
        # q=str(x)
        # rev=q[::-1]
        # if q == rev :
        #     return True
        # return False

        # method 3 not convert into string
        if x<0:
            return False
        
        original=x
        reverse=0
        while x :
            digit=x%10
            reverse=reverse*10+digit
            x//=10
        
        if original == reverse:
            return True
        
        return False



sol = Solution()
n = int(input("Enter a numer:"))
print(sol.isPalindrome(n))
