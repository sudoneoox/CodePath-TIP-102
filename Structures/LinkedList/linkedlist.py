class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None) -> None:
        """Create new Node"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> None:
        """add node to end"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value) -> None:
        """add node to beginning"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index) -> bool:
        """Add Node at specified Index"""
        if index >= self.length or index < 0:
            return False
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length - 1:
            self.append(value)
            return True

        new_node = Node(value)
        current_node = self.head
        for i in range(0, index - 1):
            current_node = current_node.next

        temp = current_node.next
        current_node.next = new_node
        new_node.next = temp

        self.length += 1
        return True

    def pop(self) -> Node | None:
        """remove tail node"""
        popped_node = None
        if self.length == 0:
            return popped_node
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            current_node = self.head

            while current_node.next is not self.tail:
                current_node = current_node.next

            current_node.next = None
            self.tail = current_node

        self.length -= 1
        return popped_node

    def pop_first(self) -> Node | None:
        """remove head from list"""
        popped_node = None
        if self.length == 0:
            return popped_node
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            tmp_node = self.head.next
            self.head.next = None
            self.head = tmp_node

        self.length -= 1
        return popped_node

    def get(self, index) -> Node | None:
        if index >= self.length or index < 0:
            return None
        current_node = self.head
        for i in range(0, index):
            current_node = current_node.next
        return current_node

    def set_value(self, index, value):
        result = self.get(index)
        if result is not None:
            result.value = value
            return True
        return None

    def print_list(self) -> None:
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
