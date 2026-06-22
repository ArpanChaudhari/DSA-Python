def isPrime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisors from 2 to √n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

n=7
print(f"{n} is Prime Number : {isPrime(n)}")