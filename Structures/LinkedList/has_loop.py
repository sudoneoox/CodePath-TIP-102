from .linkedlist import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        fast_ptr = self.head
        slow_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if fast_ptr is slow_ptr:
                return True
        return False
