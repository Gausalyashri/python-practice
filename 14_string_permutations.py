"""Problem: String Permutations
Generate all permutations of a given string using recursion
(without itertools.permutations).
"""

def permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, char in enumerate(s):
        rest = s[:i] + s[i + 1:]
        for perm in permutations(rest):
            result.append(char + perm)
    return result


if __name__ == "__main__":
    print(permutations("abc"))
