from random import randint


class Node:
    def __init__(self, value: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.value = value


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def appendNode(self, value: int) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node: Node | None = self.root
            while True:
                if current_node.value < value:
                    if current_node.right is None:
                        current_node.right = new_node
                        return True
                    current_node = current_node.right
                elif current_node.value > value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return True
                    current_node = current_node.left
                else:
                    print("Cant Insert Duplicate Values")
                    return False
        return True

    def lookup(self, value: int) -> bool:
        current: Node | None = self.root
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                break

        if current is None:
            return False
        else:
            return current.value == value


tree_root = BinarySearchTree()

for i in range(0, 10):
    randomvalue = randint(1, 100)
    print(f"Appending random value {randomvalue}")
    tree_root.appendNode(randomvalue)

inp = input("Search for Value: ")
print(tree_root.lookup(int(inp)))
