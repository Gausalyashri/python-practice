"""Problem: Armstrong Number
Check whether a number is an Armstrong (narcissistic) number,
i.e. the sum of its own digits each raised to the power of the
number of digits equals the number itself.
"""

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


if __name__ == "__main__":
    for num in [153, 370, 9474, 123]:
        print(num, is_armstrong(num))
