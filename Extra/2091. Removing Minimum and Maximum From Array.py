from typing import List
def minimumDeletions(nums: List[int]) -> int:
    n = len(nums)

    max_index = 0
    min_index = 0
    min_value = float("inf")
    max_value = float("-inf")

    for i, num in enumerate(nums):
        if num > max_value:
            max_value = num
            max_index = i

        if num < min_value:
            min_value = num
            min_index = i

    small = min(min_index, max_index)
    large = max(min_index, max_index)

    from_front = large + 1
    from_back = n - small
    front_back = (small + 1) + (n - large)

    return min(front_back, min(from_front, from_back))

nums = [2,10,7,5,4,1,8,6]
print(minimumDeletions(nums))
