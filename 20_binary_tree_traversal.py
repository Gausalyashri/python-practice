"""Problem: Binary Tree Traversals
Implement a binary tree and pre-order, in-order, and post-order
traversals (recursively).
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result


if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("preorder:", preorder(root))    # [1, 2, 4, 5, 3]
    print("inorder:", inorder(root))      # [4, 2, 5, 1, 3]
    print("postorder:", postorder(root))  # [4, 5, 2, 3, 1]
