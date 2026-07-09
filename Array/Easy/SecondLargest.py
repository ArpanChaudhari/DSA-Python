from typing import List


def secondLargest(nums: List[int]) -> int:
    max1 = float("-inf")
    max2 = float("-inf")

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    if max2 == float("-inf"):
        return -1

    return max2


nums = [7, 7, 2, 2, 10, 10, 10]
print(secondLargest(nums))
