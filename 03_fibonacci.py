"""Problem: Fibonacci Sequence
Generate the first n numbers of the Fibonacci sequence using an
efficient iterative approach (O(n) time, O(1) extra space).
"""

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    print(fibonacci(15))
