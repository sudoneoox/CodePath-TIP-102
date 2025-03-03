class Node:
    def __init__(self, value: int) -> None:
        self.next: Node | None = None
        self.value: int = value


class Queue:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.first: Node | None = new_node
        self.last: Node | None = new_node
        self.length: int = 1

    def enqueue(self, value: int) -> None:
        new_node: Node = Node(value)
        if self.first is None:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self) -> Node | None:
        ret_node: Node | None = None
        if self.length == 0:
            return ret_node
        elif self.first is self.last:
            ret_node = self.first
            self.first = None
            self.last = None
        else:
            ret_node = self.first
            self.first = self.first.next
            ret_node.next = None
        self.length -= 1
        return ret_node
