
from typing import List

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    max = -1
    list = []

    for candy in candies:
        if candy > max:
            max = candy

    for candy in candies:
        list.append(candy + extraCandies >= max)

    return list


candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = kidsWithCandies(None, candies, extraCandies)
print(result)  # Output: [True, True, True, False, True]