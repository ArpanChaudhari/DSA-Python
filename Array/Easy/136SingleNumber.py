from typing import List 
def singleNumber(nums : List[int]) -> int :
    xor = 0
    for i in nums :
        xor ^= i
    return xor

""" 
xor = 0 ^ 0 = 0
xor = 0 ^ 1 = 1
xor = 1 ^ 2 = 3  1 => 001, 2 => 010, 3 => 011 '
xor = 12 ^ 1 = 13  12 => 1100, 1 => 0001, 13 => 1101
"""

nums = [4,1,2,1,2]
print(singleNumber(nums))