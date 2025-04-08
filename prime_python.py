def primes_python(n):
    """
    Generate prime numbers up to n using Sieve of Eratosthenes.

    Args:
        n: The upper bound (exclusive)

    Returns:
        list: All prime numbers less than n
    """
    sieve = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return [x for x in range(2, n) if sieve[x]]


if __name__ == "__main__":
    print(primes_python(10))
