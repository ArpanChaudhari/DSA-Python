from typing import List


def maxSum(nums: List[int], k: int) -> int:
    MOD = 10**9 + 7

    # we count i'th set in every number
    bit_count = [0] * 32

    for n in nums:

        for i in range(32):

            # Check whether bit i is set in num
            if n & (1 << i) != 0:
                bit_count[i] += 1

    ans = 0

    # Build k numbers to maximize the sum of squares
    for _ in range(k):
        value = 0

        # collect every available bit into this number
        for i in range(32):
            if bit_count[i] > 0:
                # Set bit i in value
                value = value | (1 << i)
                bit_count[i] -= 1

        ans = (ans + value * value) % MOD

    return ans


nums = [5, 4, 3]
k = 2
print(maxSum(nums, k))  

"""
Example
nums = [5, 4, 3]
k = 2

Binary representation:
5 = 101
4 = 100
3 = 011

Step 1: Count set bits at each position

Bit 0 -> 2 times
Bit 1 -> 1 time
Bit 2 -> 2 times

bit_count = [2, 1, 2]


Step 2: Build the first number

Bit 0 available -> take it
Bit 1 available -> take it
Bit 2 available -> take it

Binary 111 = 7

Remaining counts:
Bit 0 -> 1
Bit 1 -> 0
Bit 2 -> 1


Step 3: Build the second number

Bit 0 available -> take it
Bit 1 unavailable -> skip it
Bit 2 available -> take it

Binary 101 = 5

Remaining counts:
Bit 0 -> 0
Bit 1 -> 0
Bit 2 -> 0


Step 4: Calculate the sum of squares

Answer = 7² + 5²
       = 49 + 25
       = 74

Return 74
"""
