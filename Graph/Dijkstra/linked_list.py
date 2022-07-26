from typing import Tuple


class Node:
    next = None
    value: Tuple[int, int]

    def __init__(self, value: Tuple[int, int]):
        self.value = value


class LinkedList:
    length = 0
    head = None
    tail = None

    def __init__(self, value, empty=False):
        if not empty and type(value) == int:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.length += 1

    def validate_index(self, index):
        if index is not None and not 0 <= index < self.length:
            raise ValueError("Invalid input")

    def append(self, value: Tuple[int, int]):
        new_node = Node(value)
        self.length += 1
        if self.length - 1 == 0:
            self.tail = self.head = new_node
            return
        self.tail.next = new_node  # Append node to new list
        self.tail = new_node  # Move tail to new_node

    def get_weight_by_destination(self, dest):
        # Node = tuple(destination:int, weight:int)
        temp = self.head
        for i in range(self.length):
            if temp.value[0] == dest:
                return temp.value[1]
            temp = temp.next

        return float("inf")
