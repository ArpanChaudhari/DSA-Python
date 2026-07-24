from typing import List


def largestAltitude(gain: List[int]) -> int:
    high_altitude = 0
    prefix_sum = 0
    for g in gain:
        prefix_sum += g
        high_altitude = max(high_altitude, prefix_sum)

    return high_altitude

gain = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain))