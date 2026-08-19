from typing import List
def largestInteger(nums: List[int], k: int) -> int:

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # case 1
        if k == 1:
            largest = -1

            for num in hashmap:
                if hashmap[num] == 1:
                    largest = max(largest, num)

            return largest

        # case 2
        if k == len(nums):
            return max(nums)

        # case 3
        ans = -1

        if hashmap[nums[0]] == 1:
            ans = max(ans, nums[0])

        if hashmap[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans


nums = [3,9,2,1,7]
k = 3
print(largestInteger(nums,k))