from typing import List


def nextPermutation(nums: List[int]) -> None:
    n = len(nums)

    # Step 1: Find the pivot
    pivot = -1
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            pivot = i - 1
            break

    # Step 2: If no pivot exists, reverse the whole array
    if pivot == -1:
        nums[:] = nums[::-1]
        return

    # Step 3: Find the smallest element greater than pivot
    for j in range(n - 1, pivot, -1):
        if nums[j] > nums[pivot]:
            nums[pivot], nums[j] = nums[j], nums[pivot]
            break

    # Step 4: Reverse the suffix
    nums[pivot + 1 :] = nums[pivot + 1 :][::-1]


# nums= [1,2,3,5,6,7,8]
nums = [3,2,1]
nextPermutation(nums)
print(nums)
