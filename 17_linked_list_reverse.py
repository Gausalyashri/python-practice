"""Problem: Reverse a Linked List
Implement a singly linked list and a function to reverse it
in place.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def build_linked_list(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    print(to_list(reversed_head))  # [5, 4, 3, 2, 1]
