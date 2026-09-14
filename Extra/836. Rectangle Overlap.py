from typing import List


def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:

    # rec1 is completely left of rec2
    if rec1[2] <= rec2[0]:
        return False

    # rec1 is completely right of rec2
    if rec1[0] >= rec2[2]:
        return False

    # rec1 is completely above rec2
    if rec1[1] >= rec2[3]:
        return False

    # rec1 is completely below rec2
    if rec1[3] <= rec2[1]:
        return False

    return True

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(isRectangleOverlap(rec1, rec2))  # Output: True