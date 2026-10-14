def maxSumOfSquares(num: int, sum: int) -> str:
    # Approach: 1  TC -> O(num) SC -> O(1)
    """
    number = ""

    for i in range(num):
        digit = min(9, sum)

        number += str(digit)
        sum -= digit

    if sum:
        return ""

    return number
    """

    # Approach: 2  TC -> O(num) SC -> O(1)
    if sum > 9 * num:
        return ""

    # find how many 9 can add as digit
    q, r = divmod(sum, 9)
    ans = "9" * q

    # add remaining digit
    if r > 0:
        ans += str(r)

    ans += "0" * (num - len(ans))

    return ans


num = 2
sum = 17
print(maxSumOfSquares(num, sum)) 