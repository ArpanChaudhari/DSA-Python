from typing import List


def merge(nums, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]


def mergeSort(nums: List[int], low: int, high: int):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(nums, low, mid)
    mergeSort(nums, mid + 1, high)
    merge(nums, low, mid, high)


nums=[3, 4, 5, 1, 2]
mergeSort(nums, 0, len(nums)-1)
print(nums)