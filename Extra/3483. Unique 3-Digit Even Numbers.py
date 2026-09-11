from typing import List


def totalNumbers(digits: List[int]) -> int:
    hashmap = {}
    for digit in digits:
        hashmap[digit] = hashmap.get(digit, 0) + 1

    count = 0

    for unit in range(0, 10, 2):
        if hashmap.get(unit, 0) == 0:
            continue
        hashmap[unit] -= 1

        for hundred in range(1, 10):
            if hashmap.get(hundred, 0) == 0:
                continue

            hashmap[hundred] -= 1

            for ten in range(10):
                if hashmap.get(ten, 0) == 0:
                    continue

                count += 1

            hashmap[hundred] += 1

        hashmap[unit] += 1

    return count


digits = [1,2,3,4]
print(totalNumbers(digits))  # Output: 12