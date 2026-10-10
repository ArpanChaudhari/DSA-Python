def minSumSquareDiff(nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
    diff = []
    k = k1 + k2

    for i in range(len(nums1)):
        diff.append(abs(nums1[i] - nums2[i]))

    diff.sort(reverse=True)

    if k >= sum(diff):
        return 0

    # square of 0 is zero, so it contributes nothing to the answer.
    diff.append(0)  # compares each difference with the next one

    for i in range(len(diff) - 1):

        # Operations needed to reduce the first i+1 differences from diff[i] down to diff[i+1]
        cost = (diff[i] - diff[i + 1]) * (i + 1)

        # We have enough operations to reach the next level
        if k >= cost:
            k -= cost

        # Not enough operations to reach the next level.
        else:
            # Distribute the remaining operations evenly.
            group_size = i + 1
            q = k // group_size
            r = k % group_size

            # Reduce every value in this group by q
            level = diff[i] - q

            # r values get one additional reduction & the remaining group_size-r values stay at 'level'.
            ans = r * (level - 1) ** 2 + (group_size - r) * level**2

            # Add the squares of the untouched smaller differences
            ans += sum(x * x for x in diff[i + 1 : -1])

            return ans

    return 0


nums1 = [1, 2, 3, 4]
nums2 = [2, 10, 20, 19]
k1 = 3
k2 = 4
print(minSumSquareDiff(nums1, nums2, k1, k2))