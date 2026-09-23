from typing import List


def majorityElement(nums: list[int]) -> list[int]:
    count1 = count2 = 0
    candidate1 = candidate2 = None

    # Find two majority element
    for num in nums:
        if count1 == 0 and num != candidate2:
            count1 = 1
            candidate1 = num
        elif count2 == 0 and num != candidate1:
            count2 = 1
            candidate2 = num
        elif num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # Check both are greater then n // 3
    count1 = 0
    count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        if num == candidate2:
            count2 += 1

    ans = []
    n = len(nums)
    if count1 > n // 3:
        ans.append(candidate1)

    if count2 > n // 3:
        ans.append(candidate2)

    return ans


nums = [1, 2, 1, 1, 3, 2, 2]
print(majorityElement(nums))