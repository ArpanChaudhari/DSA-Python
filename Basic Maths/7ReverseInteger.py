class Solution:
    def reverse(self, x: int) -> int:
        # if x == 0:
        #     return 0
        # elif x > 0:
        #     rev=0
        #     while x > 0:
        #         digit = x % 10
        #         rev = rev*10+digit
        #         x = x // 10
        #     if(2**31-1 < rev > -(2**31)):
        #         return 0
        #     return rev
        # else:
        #     x = -x
        #     rev=0
        #     while x > 0:
        #         digit = x % 10
        #         rev = rev*10+digit
        #         x = x // 10
        #     if(2**31-1 < rev > -(2**31)):
        #         return 0
        #     return -rev

        a = ""
        k = ""

        for i in str(x):
            if i.isdigit():
                k += str(i)
            else:
                a += str(i)

        q = int(a + k[::-1])

        if q > (2**31) - 1 | q < -(2 * 31):
            return 0
        
        return q


sol = Solution()
n = int(input("Enter a numer:"))
print(sol.reverse(n))
