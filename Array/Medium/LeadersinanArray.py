from typing import List


def leaders(nums: List[int]) -> List[int]:
    output = [nums[-1]]
    leader = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > leader:
            leader = nums[i]
            output.append(leader)

    return output[::-1]


nums = [1, 2, 5, 3, 1, 2]
print(leaders(nums))