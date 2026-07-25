from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    # Method 1
    answer = [[], []]       # [[]]*2 actually creates two references to the same list.Point to the same list object.
    set1, set2 = set(nums1), set(nums2)

    for num in set1:
        if num not in set2:
            answer[0].append(num)

    for num in set2:
        if num not in set1:
            answer[1].append(num)

    return answer

    # Method 2
    # return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]

nums1 = [1,2,3] 
nums2 = [2,4,6]
print(findDifference(nums1,nums2))