class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None


class Stack:
    def __init__(self, value: int) -> None:
        new_node: Node = Node(value)
        self.top: Node | None = new_node
        self.height: int = 1

    def push(self, value) -> None:
        new_node: Node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self) -> Node | None:
        ret_node: Node | None = None
        if self.height == 0:
            return ret_node
        else:
            ret_node = self.top
            self.top = self.top.next
        self.height -= 1
        return ret_node
