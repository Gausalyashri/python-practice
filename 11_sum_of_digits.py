"""Problem: Sum of Digits
Compute the sum of the digits of a non-negative integer.
"""

def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == "__main__":
    print(sum_of_digits(9875))  # 29
