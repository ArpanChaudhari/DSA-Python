from typing import List
class Solution():
    def printDivisior(self,n:int)-> List[int]:
        small=[]
        large=[]

        # Iterate only up to √n
        for i in range(1,int(n**0.5)+1):  # Time Complexity = O(√n)
            if n%i==0:
                small.append(i)

                # This avoids duplicates for perfect squares
                if i!=n//i:
                    large.append(n//i)  
        
        return small + large[::-1] # # Reverse large to get divisors in ascending order
    
n=36
sol=Solution()
k=sol.printDivisior(n)
print(k)