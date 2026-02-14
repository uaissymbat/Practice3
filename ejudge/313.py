numbers = list(map(int, input().split()))

primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))

if primes:
    print(' '.join(map(str, primes)))
else:
    print("No primes")