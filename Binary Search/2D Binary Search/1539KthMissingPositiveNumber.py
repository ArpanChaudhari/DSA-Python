from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2
        miss = arr[mid] - (mid + 1)

        if miss < k:
            low = mid + 1
        else:
            high = mid - 1

    return high + k + 1

arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr,k))