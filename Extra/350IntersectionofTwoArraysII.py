from typing import List


def intersect( nums1: List[int], nums2: List[int]) -> List[int]:
    hashset = {}

    common = []
    for i in nums1:
        hashset[i] = hashset.get(i, 0) + 1

    for i in nums2:
        if i in hashset and hashset[i] > 0:
            common.append(i)
            hashset[i] -= 1

    return common


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2)) 