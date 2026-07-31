"""Problem: Prime Check
Determine whether a given integer is a prime number, using trial
division up to sqrt(n) for efficiency.
"""

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    primes = [x for x in range(2, 50) if is_prime(x)]
    print(primes)
