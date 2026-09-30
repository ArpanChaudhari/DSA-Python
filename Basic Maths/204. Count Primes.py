def countPrimes(n: int) -> int:
    # Assume every number is prime initially
    is_prime = [True] * n

    # 0 and 1 are not prime
    if n > 0:
        is_prime[0] = False
    if n > 1:
        is_prime[1] = False

    # We only need to check up to sqrt(n)
    for number in range(2, int(n**0.5) + 1):

        # If number is prime, mark all its multiples as not prime
        if is_prime[number]:

            # Start from number * number
            for multiple in range(number * number, n, number):
                is_prime[multiple] = False

    # Count all numbers that are still marked as prime
    return sum(is_prime)

n = 100
print(countPrimes(n))