from typing import List

def add_if_unique(ans: List[int], value: int) -> None:
    # Append only if answer is empty or value is different
    # from the last inserted element
    if not ans or ans[-1] != value:
        ans.append(value)


def union(nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []

    n1, n2 = len(nums1), len(nums2)
    left = right = 0

    # Merge both arrays using two pointers
    while left < n1 and right < n2:

        if nums1[left] <= nums2[right]:
            add_if_unique(ans, nums1[left])
            left += 1
        else:
            add_if_unique(ans, nums2[right])
            right += 1

    # Add remaining elements from nums1
    while left < n1:
        add_if_unique(ans, nums1[left])
        left += 1

    # Add remaining elements from nums2
    while right < n2:
        add_if_unique(ans, nums2[right])
        right += 1

    return ans


nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]

print(union(nums1, nums2))