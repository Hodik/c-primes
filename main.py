import sys
import time

import prime_python

import prime_c


def benchmark_function(func, *args):
    """Measure execution time of a function"""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def main():
    test_sizes = [100000, 1000000, 10000000]

    print("Benchmarking Prime Number Generation")
    print("===================================")

    for n in test_sizes:
        print(f"\nGenerating primes up to {n:,}:")

        # Python implementation
        print("\nPython implementation:")
        py_primes, py_time = benchmark_function(prime_python.primes_python, n)
        print(f"Found {len(py_primes)} primes in {py_time:.4f} seconds")

        # C implementation
        print("\nC implementation:")
        c_primes, c_time = benchmark_function(prime_c.primes_c, n)
        print(f"Found {len(c_primes)} primes in {c_time:.4f} seconds")

        # Compare results and performance
        if len(py_primes) == len(c_primes):
            print(f"\nVerified: Both implementations found {len(py_primes)} primes")
            speedup = py_time / c_time
            print(f"Speedup: {speedup:.2f}x faster with C")
        else:
            print(
                f"ERROR: Different number of primes found! Python: {len(py_primes)}, C: {len(c_primes)}"
            )
            if len(py_primes) > 0 and len(c_primes) > 0:
                print(f"Python first 5: {py_primes[:5]}")
                print(f"C first 5: {c_primes[:5]}")


if __name__ == "__main__":
    try:
        import prime_c
    except ImportError:
        print("Error: prime_c module not found!")
        print(
            "Please build the C extension first with: python setup_prime.py build_ext --inplace"
        )
        sys.exit(1)

    main()
