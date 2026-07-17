from typing import List
def rearrangeArray(nums: List[int]) -> List[int]:
    pos = 0
    neg = 1
    merge= [0]*len(nums)

    for num in nums :
        if num < 0 :
            merge[neg] = num
            neg += 2 
        else :
            merge[pos] = num 
            pos += 2
    
    return merge


nums = [3,1,-2,-5,2,-4]
result = rearrangeArray(nums)
print(result)