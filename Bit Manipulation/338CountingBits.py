from typing import List


def countBits(n: int) -> List[int]:
    bits = [0] * (n + 1)

    for i in range(1, n + 1):
        bits[i] = bits[i & (i - 1)] + 1

    return bits

n = 7
print(countBits(n))

"""
0 has 0 set bit then,
1 has 1 set bit -> bits[n & (n-1)] + 1
2 has 1 set bit ->  bits[2 & 1] + 1 -> bits[0] + 1
3 hase 2 set bit -> bits[3 & 2] + 1 -> bits[1] + 1
"""