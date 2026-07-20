from typing import List


def longestConsecutive(nums: List[int]) -> int:
    maxlength = 0

    hashset = set(nums)

    for num in hashset:
        if num - 1 not in hashset:
            length = 1
            while num + length in hashset:
                length += 1
            maxlength = max(maxlength, length)

    return maxlength


nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))