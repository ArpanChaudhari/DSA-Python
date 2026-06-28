from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)

    common = []

    if len(set1) <= len(set2):
        for i in set1:
            if i in set2:
                common.append(i)
    else:
        for j in set2:
            if j in set1:
                common.append(j)

    return common

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2)) 