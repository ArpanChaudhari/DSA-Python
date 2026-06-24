from typing import List


def removeElement(nums: List[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


list=[1,2,3,2,1,2]
val=2
k=removeElement(list,val)
print(k)