class Solution:
    def countDigit(self,N : int) -> int :
        count=0
        if N == 0:
            return 1
        while N > 0:
            count+=1
            N//=10
        
        return count

n=int(input("Enter a Number:"))   
sol=Solution()
print(f"Digit of number : {sol.countDigit(n)}")