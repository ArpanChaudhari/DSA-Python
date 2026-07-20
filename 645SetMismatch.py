from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)

    i = 0
    while i < n:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]


nums = [4, 3, 3, 1]
print(findErrorNums(nums))
