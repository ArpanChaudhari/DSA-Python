from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    hashmap = {}

    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    return len(hashmap) == len(set(hashmap.values()))


arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))