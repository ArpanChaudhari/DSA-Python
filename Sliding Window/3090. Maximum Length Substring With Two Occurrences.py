class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        # Version 1
        # hashmap = {s[0]:1}
        # max_length = 1
        # left = 0
        # right = 1
        # while right < len(s):
        #     if s[right] not in hashmap or hashmap[s[right]] < 2:
        #         hashmap[s[right]] = hashmap.get(s[right],0)+1
        #         max_length = max(max_length, right - left + 1)
        #     else:
        #         while s[left] != s[right]:
        #             hashmap[s[left]] -= 1
        #             left += 1

        #         # remove the previous occurrence of s[right]
        #         hashmap[s[left]] -= 1
        #         left += 1

        #         # add current s[right]
        #         hashmap[s[right]] += 1

        #     right += 1

        # return max_length

        # Version 2

        freq = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Add the character first
            freq[s[right]] = freq.get(s[right], 0) + 1

            # While the window is invalid, shrink it
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


Sol = Solution()

s = "bcbbbcba"
print(Sol.maximumLengthSubstring(s))
