from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    n = len(height)
    right = n - 1
    max_water = 0

    while right > left:
        a = min(height[left], height[right])
        b = right - left
        max_water = max(max_water, a * b)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


height = [3,1,2,4,5]
print(maxArea(height))