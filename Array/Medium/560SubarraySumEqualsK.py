from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    hashmap = {0: 1}
    count = 0
    prefix_sum = 0
    for num in nums:
        prefix_sum += num

        # Check if there exists a previous prefix sum.such that current_prefix - previous_prefix = k
        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]

        # Store current prefix sum
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count

nums = [1,-1,1,-1]
k = 0
print(subarraySum(nums,k))