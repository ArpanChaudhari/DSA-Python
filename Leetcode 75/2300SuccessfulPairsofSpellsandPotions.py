from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    n = len(spells)
    m = len(potions)

    potions.sort()

    for i in range(n):
        low = 0
        high = m - 1
        ans = m

        while low <= high:
            mid = low + (high - low) // 2
            pos = potions[mid] * spells[i]

            if pos >= success:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        spells[i] = m - ans

    return spells

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells,potions,success))