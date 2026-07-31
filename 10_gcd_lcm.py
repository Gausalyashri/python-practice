"""Problem: GCD and LCM
Compute the greatest common divisor and least common multiple
of two integers.
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0


if __name__ == "__main__":
    print(gcd(48, 18))   # 6
    print(lcm(4, 6))     # 12
