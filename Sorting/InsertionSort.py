from typing import List
""" 
Insertion Sort (Swap Based

Assume the first element is already sorted.
Start from the second element (`i = 1`).
Compare the current element with elements on its left.
If the left element is larger, swap them.
Continue moving the element left until it reaches its correct position.

Example:

`[13, 45, 35, 25, 29, 9]`

`i = 1`, `45 > 13` → no swap.
`i = 2`, `35 < 45` → swap → `[13, 35, 45, 25, 29, 9]`
`i = 3`, `25 < 45` → swap, `25 < 35` → swap
  → `[13, 25, 35, 45, 29, 9]`
`i = 4`, `29 < 45` and `29 < 35` → swap until correct position.
`i = 5`, `9` is swapped left repeatedly until it reaches the beginning.

After each iteration, the left part `nums[0...i]` becomes sorted.

Outer loop:
`for i in range(1, n)`

Inner loop:
`while j > 0 and nums[j-1] > nums[j]`

The condition `j > 0` prevents accessing `nums[-1]` unintentionally while comparing `nums[j-1]` and `nums[j]`.
"""
def InsertionSort(nums:List[int]):
    for i in range(1,len(nums)):
        j=i
        while j>0 and nums[j-1]>nums[j]:
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j-=1

nums = [1, 5, 3, 9, 6]
print("Before Using Insertion Sort:")
print(nums)
InsertionSort(nums)
print("After Using Insertion Sort:")
print(nums)

# Time complexity O(n2) in worst case and best case