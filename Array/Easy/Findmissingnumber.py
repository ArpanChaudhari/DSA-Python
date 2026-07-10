from typing import List

def missingNumber(nums : List[int])-> int :
    n = len(nums)

    # use sequence formula 
    sum =( n * (n+1))//2

    for num in nums :
        sum -= num 
    
    return sum


nums = [3, 0, 1]
print(missingNumber(nums))