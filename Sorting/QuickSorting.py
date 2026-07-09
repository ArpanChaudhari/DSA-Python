from typing import List


def quicksort(nums: List[int], low: int, high: int):
    if low < high:
        partition_index = partition(nums, low, high)

        quicksort(nums, low, partition_index - 1)
        quicksort(nums, partition_index + 1, high)


def partition(nums, low, high):
    i = low
    j = high
    pivot = nums[high]

    while i < j:

        while nums[i] < pivot and i <= high:
            i += 1

        while nums[j] > pivot and j >= low:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        
    
    nums[i],pivot = pivot,nums[i]

    return i

arr = [10, 7, 8, 9, 1, 5]
print("Before quick sort :",arr)
quicksort(arr,0,len(arr)-1)
print("After quick sort:",arr)