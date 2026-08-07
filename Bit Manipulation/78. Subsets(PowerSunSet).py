from typing import List


def powerSet(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    for num in range(2**n): # iterate from 0 to no. of power set -1
        list = []
        for i in range(n): # iterate nums
            if num & (1 << i): # check i'th bit if 1 then add else ignore
                list.append(nums[i])

        ans.append(list)

    return ans


nums = [1, 2, 3]
print(powerSet(nums))
