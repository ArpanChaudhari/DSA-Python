from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:

    n = len(nums)

    ans = [1] * n  # creates an array of size n with all elements initialized to 1

    # Calculate the product of all elements to the left of each index
    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]

    # assign a variable to keep track of the product from right to left traversal
    right = 1

    # traverse the array from right to left and update the ans array with the product of elements to the right of each index
    for j in range(n - 1, -1, -1):
        ans[j] = ans[j] * right
        right *= nums[j]

    return ans


nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))  # Output: [0, 0, 9, 0, 0]
