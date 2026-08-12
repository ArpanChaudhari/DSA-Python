from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = []
    i = 0
    while i < n:
        x = nums[i]

        if nums[x - 1] != x:
            nums[i], nums[x - 1] = nums[x - 1], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            ans.append(i + 1)

    return ans

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))