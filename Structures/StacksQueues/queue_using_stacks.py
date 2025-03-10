from typing import List


class MyQueue:
    def __init__(self):
        self.stack1: List[int | str] = []
        self.stack2: List[int | str] = []

    def enqueue(self, value: int | str) -> None:
        if self.stack1 is None:
            self.stack1.append(value)
        else:
            while not self.is_empty():
                self.stack2.append(self.peek())
                self.stack1.pop()
            self.stack1.append(value)
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())

    def dequeue(self) -> None | str | int:
        if self.is_empty():
            return None
        else:
            return self.stack1.pop()

    def peek(self) -> int | str:
        return self.stack1[-1]

    def is_empty(self) -> int:
        return len(self.stack1) == 0


# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""
