from typing import List
def maximumProduct(nums: List[int]) -> int:
    la1 = la2 = la3 = float("-inf")
    sm1 = sm2 = float("inf")

    for i in nums:

        if i > la1:
            la3 = la2
            la2 = la1
            la1 = i
        elif i > la2:
            la3 = la2
            la2 = i
        elif i > la3:
            la3 = i

        if i < sm1:
            sm2 = sm1
            sm1 = i
        elif i < sm2:
            sm2 = i

    return max(la1 * la2 * la3, la1 * sm1 * sm2)

list = [-100,-90,-1,2,3,4]
result = maximumProduct(list)
print(result)