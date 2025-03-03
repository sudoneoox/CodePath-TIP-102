class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key) -> int:
        """Hashing Function"""
        my_hash: int = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self) -> None:
        """Prints Hash Table"""
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key: str, value: int) -> None:
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = value
        else:
            while self.data_map[index] is not None:
                index += 1
                if index > 6:
                    index = 0
            self.data_map[index] = value

