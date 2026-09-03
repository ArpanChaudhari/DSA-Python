from typing import List


def uniformArray(nums1: list[int]) -> bool:

    # Solution 1

    '''
    smallest_odd = float("inf")

    # Find smallest odd number
    for num in nums1:
        if num % 2 == 1:
            smallest_odd = min(smallest_odd, num)

    # If no odd number, all are already even
    if smallest_odd == float("inf"):
        return True

    # Every even number must be greater than smallest odd
    for num in nums1:
        if num % 2 == 0 and num < smallest_odd:
            return False

    return True
    '''

    # Solution 2
    # find min element
    m = min(nums1)
    if m&1:
        return True # if min element is odd, we can make all element odd
    for n in nums1:
        if n&1:
            return False # if min element is not odd, so we need all element even else we can't make all element even 

        return True # if no odd element found, we can make all element even


nums1 = [1,4,7]
print(uniformArray(nums1))
