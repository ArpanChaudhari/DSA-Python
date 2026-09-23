from typing import List


def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    prefix = 1
    suffix = 1

    max_Product = nums[0]

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n - i - 1]

        max_Product = max(max_Product, suffix, prefix)

    return max_Product

nums = [1, -2, 3, 4, -4, -3]
print(maxProduct(nums))