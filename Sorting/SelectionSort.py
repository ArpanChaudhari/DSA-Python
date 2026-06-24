from typing import List


def SelectionSort(nums: List[int]):
    for i in range(len(nums)):  # iterate through all the array element
        # select first element as minimum
        Min_index = i

        # Find the minimum element in the remaining array
        for j in range(i + 1, len(nums)):

            if nums[j] < nums[Min_index]:
                Min_index = j  # Update min_index if smaller is found

        # Swap the found minimum with the first element of unsorted part
        nums[i], nums[Min_index] = nums[Min_index], nums[i]


nums = [1, 5, 3, 9, 6]
SelectionSort(nums)
print(nums)
