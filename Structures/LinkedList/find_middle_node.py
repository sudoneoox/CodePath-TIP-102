from .linkedlist import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        """
        Return Middle Node
        If node has an even number of nodes return the first node of
        the second half of the list
        """
        # Fast Pointer Slow Pointer Approach
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None:
            if fast_ptr.next is None:
                break
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

