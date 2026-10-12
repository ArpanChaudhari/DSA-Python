from typing import List


def findKOr(nums: List[int], k: int) -> int:
    bit_count = [0] * 32

    for n in nums:
        for i in range(32):
            if n & (1 << i):
                bit_count[i] += 1

    value = 0
    for i in range(32):
        if bit_count[i] >= k:
            value = value | (1 << i)

    return value

nums = [7, 12, 9, 8, 9, 15]
k = 4
print(findKOr(nums, k))  


"""
nums = [7, 12, 9, 8, 9, 15]
k = 4

Binary representation:
7  = 0111
12 = 1100
9  = 1001
8  = 1000
9  = 1001
15 = 1111

Step 1: Count set bits

Bit 0 -> 4 times
Bit 1 -> 2 times
Bit 2 -> 3 times
Bit 3 -> 6 times

Step 2: Check which bits appear at least k = 4 times

Bit 0 -> 4 >= 4 -> Include
Bit 1 -> 2 < 4  -> Skip
Bit 2 -> 3 < 4  -> Skip
Bit 3 -> 6 >= 4 -> Include

Step 3: Build the answer

Bit 0 = 1
Bit 3 = 8

Answer = 1 + 8 = 9

Return 9
"""