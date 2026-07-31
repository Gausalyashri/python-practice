"""Problem: Anagram Check
Determine whether two strings are anagrams of each other
(same letters, same frequency, ignoring case and spaces).
"""

from collections import Counter


def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))          # True
    print(is_anagram("Dormitory", "Dirty Room"))    # True
    print(is_anagram("hello", "world"))             # False
