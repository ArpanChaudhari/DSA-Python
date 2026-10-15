from typing import List


def sumCounts(nums: List[int]) -> int:
    n = len(nums)

    result = 0

    for i in range(n):

        ans = set()

        for j in range(i, n):
            ans.add(nums[j])
            result += len(ans) ** 2

    return result


nums = [1, 2, 3]
print(sumCounts(nums))  