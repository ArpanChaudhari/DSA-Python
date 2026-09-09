def countCommas(n: int) -> int:

    count = 0
    # commas start from 4 digit (1,000)
    start = 1000

    while start <= n:
        count += n - start + 1

        start *= 1000

    return count

    """
        at first count how many numbers each contribute one comma.
        then odd numbers contribute one additional comma.
        and so on
        """

n = 9999999999
print(countCommas(n))  # output 28998999000
