from typing import List
""" 
Bubble Sort:

Adjacent elements are compared and swapped if they are in the wrong order.
After the first pass, the largest element moves to the last position.

Example:
`[13, 45, 35, 25, 29, 9]`

First pass:
`13,45` ✓ → `45,35` swap → `45,25` swap → `45,29` swap → `45,9` swap

Result after first pass:
`[13, 35, 25, 29, 9, 45]`

Since `45` is already in its correct position, we don't need to check it again.

Outer loop runs from `i = n-1` down to `0`.

Inner loop runs from `j = 0` to `j < i`.

We use 'range(i-1) instead of `range(i) to avoid accessing `arr[j+1]` outside the array bounds (`arr[6]` in this example).

"""

def BubbleSort(nums: List[int]):  # Compare adjacent elements and swap them if arr[j] > arr[j+1].

    Did_swap = False
    for i in range(len(nums) - 1, -1, -1):
        
        for j in range(i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                Did_swap = True
        if Did_swap == False :
            return

nums = [1, 5, 3, 9, 6]
print("Before Using Bubble Sort:")
print(nums)
BubbleSort(nums)
print("After Using Bubble Sort:")
print(nums)

# Time complexity O(n2) in worst case and O(n) in best case