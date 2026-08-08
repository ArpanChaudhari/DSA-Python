from typing import List


def singleNumber(nums: List[int]) -> List[int]:
    xor1 = 0

    # XOR all numbers
    for num in nums:
        xor1 = xor1 ^ num

    # Find rightmost set bit
    setbit = xor1 & (-xor1)

    bucket1 = 0
    bucket2 = 0

    # Divide numbers into two groups
    for num in nums:
        if num & setbit:
            bucket1 = bucket1 ^ num
        else:
            bucket2 = bucket2 ^ num

    return [bucket1, bucket2]


nums = [1,2,1,3,2,5]
print(singleNumber(nums))