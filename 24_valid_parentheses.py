"""Problem: Valid Parentheses
Given a string containing just the characters '(', ')', '{',
'}', '[' and ']', determine if the input string is valid
(every opening bracket is closed by the same type, in the
correct order), using a stack.
"""

def is_valid_parentheses(s):
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


if __name__ == "__main__":
    print(is_valid_parentheses("()[]{}"))  # True
    print(is_valid_parentheses("(]"))      # False
    print(is_valid_parentheses("([{}])"))  # True
