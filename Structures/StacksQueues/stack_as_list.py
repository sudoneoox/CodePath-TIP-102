from typing import List


class Stack:
    def __init__(self) -> None:
        self.stack_list: List[int | str] = []

    def print_stack(self) -> None:
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def push(self, value: int | str) -> None:
        self.stack_list.append(value)

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def peek(self) -> int | str | None:
        """Returns last element"""
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self) -> int:
        return len(self.stack_list)

    def pop(self) -> None | int | str:
        if self.is_empty():
            return None
        else:
            ret_value: int | str = self.stack_list.pop()
            return ret_value
