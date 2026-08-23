from typing import List
def resultArray(nums: List[int]) -> List[int]:
    arr1 = [nums[0]]
    arr2 = [nums[1]]

    for i in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])

    return arr1 + arr2


nums = [5, 4, 3, 8]
print(resultArray(nums))