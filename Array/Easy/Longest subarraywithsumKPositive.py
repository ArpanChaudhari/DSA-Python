def longestSubarray(nums, k):
    sum = 0
    left = 0
    max_len = 0
    for right in range(len(nums)):
        sum += nums[right]
        while sum > k:
            sum -= nums[left]
            left += 1

        if sum == k:
            max_len = max(max_len, (right - left) + 1)

    return max_len


nums = [2, 1, 1, 1, 2]
k = 3
print(longestSubarray(nums, k))