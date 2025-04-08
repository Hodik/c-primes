import prime_c

if __name__ == "__main__":
    print(prime_c.primes_c(10))
    l = prime_c.primes_c(10)
    l.append(100)

    print(l.__class__)
