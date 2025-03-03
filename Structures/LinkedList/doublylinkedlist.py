from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.data: Any = value
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node: Node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length: int = 1

    def append(self, value: Any) -> None:
        """Appends to the end of the linked list"""
        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head is self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> Node | None:
        """Deletes at the end of the list and returns deleted node"""
        retNode: Node | None = None
        if self.length == 0:
            return retNode
        elif self.length == 1:
            retNode = self.head
            self.head = None
            self.tail = None
        else:
            retNode = self.tail
            tmpNode = self.tail.prev
            tmpNode.next = None
            self.tail.prev = None
            self.tail = tmpNode
        self.length -= 1
        return retNode

    def prepend(self, value: Any) -> None:
        """Appends to the beginning of the linked list"""
        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self) -> Node | None:
        """Removes head node"""
        retNode: Node | None = None
        if self.length == 0:
            return retNode
        elif self.length == 1:
            retNode = self.head
            self.head = None
            self.tail = None
        else:
            retNode = self.head
            tmpNode = self.head.next
            self.head.next = None
            tmpNode.prev = None
            self.head = tmpNode
        self.length -= 1
        return retNode

    def get(self, index: int) -> Node | None:
        """Gets node at specified index"""
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        else:
            if self.length - index <= self.length // 2:
                current_node = self.head
                for _ in range(0, index):
                    current_node = current_node.next
                return current_node
            else:
                current_node = self.tail
                for _ in range(0, index):
                    current_node = current_node.prev
                return current_node

    def set_value(self, index: int, value: Any) -> bool:
        tmpNode = self.get(index)
        if tmpNode is None:
            return False
        tmpNode.value = value
        return True

    def insert(self, index: int, value: Any) -> bool:
        if index > self.length or index < 0:
            return False
        elif index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node: Node = Node(value)
            before: Node = self.get(index - 1)
            after = before.next
            before.next = new_node
            new_node.prev = before
            new_node.next = after
            after.prev = new_node
            self.length += 1

        return True

    def remove(self, index: int) -> Node | None:
        ret_node: Node | None = None
        if index >= self.length or index < 0:
            ret_node = None
        elif index == 0:
            ret_node = self.pop_first()
        elif index == self.length - 1:
            ret_node = self.pop()
        else:
            before: Node | None = self.get(index - 1)
            ret_node = before.next
            before.next = ret_node.next
            ret_node.next.before = before
            ret_node.next = None
            ret_node.before = None
            self.length -= 1
        return ret_node
