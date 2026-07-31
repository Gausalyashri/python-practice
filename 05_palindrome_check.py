"""Problem: Palindrome Check
Check whether a given string is a palindrome, ignoring case,
spaces, and punctuation.
"""

import re


def is_palindrome(s):
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("Hello, World!"))                    # False
