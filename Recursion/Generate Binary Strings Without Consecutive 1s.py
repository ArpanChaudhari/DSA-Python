from typing import List


def generate(current, prev_one, n, result):
    if len(current) == n:
        result.append(current)
        return

    if prev_one:
        generate(current + "0", False, n, result)

    else:
        generate(current + "0", False, n, result)

        generate(current + "1", True, n, result)

    return result


def generateString(N: int) -> List[str]:
    # write your code here
    result = []
    curr = ""

    return generate(curr, False, N, result)


n = 8
result = generateString(n)
print(result)
