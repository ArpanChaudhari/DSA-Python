from typing import List


def sumOfSquares(nums: List[int]) -> int:
    sp_sum = 0
    n = len(nums)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:

            sp_sum += nums[i - 1] ** 2

            pair = n // i

            if pair != i:
                sp_sum += nums[pair - 1] ** 2

    return sp_sum


nums = [4,5,6,7]
print(sumOfSquares(nums))