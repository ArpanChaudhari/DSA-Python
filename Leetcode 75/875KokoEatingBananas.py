from typing import List
from math import ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    # find max length pile
    maxPile = max(piles)

    # Bs from 1 to max pile
    low, high = 1, maxPile

    # maximum ans possible
    ans = maxPile

    while low <= high:
        mid = low + (high - low) // 2

        # call function to calculate Time
        toHour = calculateHour(piles, mid)

        if toHour <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def calculateHour(piles, speed):
    toHour = 0

    # calculate total time by distance / speed
    for pile in piles:
        toHour += ceil(pile / speed)  # ceil max eating hour

    return toHour

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))