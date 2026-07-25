def maxProduct(n: int) -> int:
    max_product = 0
    digit1 = n % 10
    n = n // 10

    while n > 0:
        digit2 = n % 10
        max_product = max(max_product, digit1 * digit2)
        digit1 = max(digit1, digit2)
        n = n // 10

    return max_product

n = 437
print(maxProduct(n))