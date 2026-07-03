from collections import deque

class MyStack:
    def __init__(self):
        # Initialize as an empty double-ended queue
        self.q = deque()

    def push(self, x: int) -> None:
        # Adds element to the end (top of stack)
        self.q.append(x)

    def pop(self) -> int:
        # Removes element from the same end (LIFO)
        return self.q.pop()

    def top(self) -> int:
        # Returns the last element added
        return self.q[-1]

    def empty(self) -> bool:
        # Returns True if queue is empty
        return len(self.q) == 0