from typing import List


def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

    # If no flowers need to be planted, answer is always True
    if n == 0:
        return True

    length = len(flowerbed)
    i = 0

    while i < length:

        # Treat out-of-bound neighbors as empty plots
        left_empty = i == 0 or flowerbed[i - 1] == 0
        right_empty = i == length - 1 or flowerbed[i + 1] == 0

        # Can plant only if current and both neighbors are empty
        if flowerbed[i] == 0 and left_empty and right_empty:

            # Plant flower greedily
            flowerbed[i] = 1
            n -= 1

            # If we already planted enough flowers, return immediately
            if n == 0:
                return True

            # Adjacent plot cannot be used now, so skip it
            i += 2
        else:
            # Move to next position
            i += 1

    # If we couldn't plant all required flowers
    return False


flowerbed = [1,0,0,0,1]
n = 1
result = canPlaceFlowers(None, flowerbed, n)
print(result)  # Output: True