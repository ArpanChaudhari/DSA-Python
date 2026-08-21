"""Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.
"""

# def countSubstring(s: str, k: int) -> int:
#     total = 0
#     for left in range(len(s)-k + 1):
#         hashmap = {}
#         for right in range(left, len(s)):
#             hashmap[s[right]] = hashmap.get(s[right], 0) + 1

#             if len(hashmap) == k:
#                 total += 1

#     return total


def atMostK(s, k):
    left = 0
    total = 0
    hashmap = {}

    for right in range(len(s)):
        hashmap[s[right]] = hashmap.get(s[right], 0) + 1

        while len(hashmap) > k:
            hashmap[s[left]] -= 1
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1

        total += (right - left + 1)

    return total


def countSubstring(s: str, k: int) -> int:
    return atMostK(s, k) - atMostK(s, k - 1)


s = "abcbaa"
k = 3

print(countSubstring(s, k))
