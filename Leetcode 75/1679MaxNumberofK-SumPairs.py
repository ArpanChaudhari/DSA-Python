from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    hashmap = {}
    count = 0
    for num in nums:
        if k - num in hashmap and hashmap[k - num] > 0:
            count += 1
            hashmap[k - num] -= 1
        else:
            hashmap[num] = hashmap.get(num, 0) + 1
    return count


# nums = [1,2,3,4]
# k = 5
nums = [1,1,1,4]
k =5
print(maxOperations(nums,k))