"""Problem: Factorial
Compute n! (the factorial of a non-negative integer n) both iteratively
and recursively.
"""

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print(factorial_iterative(10))   # 3628800
    print(factorial_recursive(10))   # 3628800
