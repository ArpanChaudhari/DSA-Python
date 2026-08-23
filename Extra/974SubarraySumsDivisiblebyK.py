from typing import List


def subarraysDivByK(nums: List[int], k: int) -> int:
    hashmap = {0: 1}
    count = 0
    prefix_sum = 0
    for num in nums:
        prefix_sum += num

        if prefix_sum % k in hashmap:
            count += hashmap[prefix_sum % k]

        hashmap[prefix_sum % k] = hashmap.get(prefix_sum % k, 0) + 1

    return count

nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums,k))