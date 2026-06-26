from typing import List


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    last_seen = {}

    for i in range(len(nums)):
        if nums[i] in last_seen:
            if i - last_seen[nums[i]] <= k:
                return True

        last_seen[nums[i]] = i

    return False


nums = [1, 2, 3, 1]
k = 3   
c = containsNearbyDuplicate(None, nums, k)
print(c)