from typing import List


class Solution:

    # Method 1
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     first = self.find_first(nums,target)
    #     last = self.find_last(nums,target)
    #     return [first, last]

    # def find_first(self, nums, target):
    #     low = 0
    #     high = len(nums) - 1
    #     ans = -1

    #     while low <= high :
    #         mid = (low + high) // 2

    #         if nums[mid] == target:
    #             ans = mid
    #             high = mid - 1
    #         elif nums[mid] > target:
    #             high = mid - 1
    #         else:
    #             low = mid + 1

    #     return ans

    # def find_last(self, nums, target):
    #     low = 0
    #     high = len(nums) - 1
    #     ans = -1

    #     while low <= high :
    #         mid = (low + high) // 2

    #         if nums[mid] == target :
    #             ans = mid
    #             low = mid + 1
    #         elif nums[mid] > target:
    #             high = mid - 1
    #         else :
    #             low = mid + 1

    #     return ans

    # Method 2
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)
        return [first, last]

    def binarySearch(self, nums, target, isFirst):
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ans = mid

                if isFirst:
                    high = mid - 1  # Continue searching left
                else:
                    low = mid + 1  # Continue searching right

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return ans


sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(sol.searchRange(nums, target))
