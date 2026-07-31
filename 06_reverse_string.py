"""Problem: Reverse a String
Reverse a given string without using Python's built-in reversed()
or slicing shortcuts (implemented manually with a two-pointer swap).
"""

def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


if __name__ == "__main__":
    print(reverse_string("hello world"))
