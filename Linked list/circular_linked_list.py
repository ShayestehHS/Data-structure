from typing import Any, Iterator, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional[Node] = None

    def __str__(self):
        return self.data

class CircularLinedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __iter__(self) -> Iterator[Any]:
        node: Node = self.head
        while node != self.tail:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tupel(iter(self)))

    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def is_empty(self) -> bool:
        return len(self) == 0

    def check_index(self, index: int):
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range.")

    def insert_tail(self, data: Any):
        return self.insert_at(index=len(self) - 1, data=data)

    def insert_head(self, data: Any):
        return self.insert_at(index=0, data=data)

    def insert_at(self, index: int, data: Any):
        self.check_index(index)

        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if index == len(self) - 1:
                self.tail = new_node

    def delete_tail(self) -> Node:
        return self.delete_from(len(self) - 1)

    def delete_head(self) -> Node:
        return self.delete_from(0)

    def delete_from(self, index: int) -> Node:
        self.check_index(index)

        result: Node = self.head
        if self.head == self.tail:  # Only one node is exists
            self.head = self.tail = None
        elif index == 0:
            self.tail.next = self.head.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(0, index - 1):
                temp = temp.next
            result = temp.next
            if result == self.tail:
                temp.next = temp.next.next
                self.tail = temp
        return result
