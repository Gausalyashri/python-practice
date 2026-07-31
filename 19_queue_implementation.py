"""Problem: Queue Implementation
Implement a Queue data structure (FIFO) supporting enqueue,
dequeue, peek, is_empty, and size operations using
collections.deque for O(1) operations.
"""

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.dequeue())  # a
    print(q.peek())     # b
    print(q.size())     # 2
