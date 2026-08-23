from typing import List


def containDuplicate(nums: List[int]) -> bool:
    # let take HashSet
    seen = set()
    # iterate over loop
    for i in nums:
        # Check element is in HashSet
        if i in seen:
            return True
        # Add element in HashSet
        seen.add(i)

    return False


nums=[1,2,3,1]
print(containDuplicate(nums))