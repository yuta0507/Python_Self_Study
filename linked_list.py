from __future__ import annotations
from typing import Any

class Node(object):
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data: Any = data
        self.next: Node = next_node

class LinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head: Node = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        prev_node = self.head
        current_node = self.head.next

        while True:
            if current_node.data == data:
                prev_node.next = current_node.next
                return

            if current_node.next is None:
                return

            prev_node = current_node
            current_node = current_node.next


if __name__ == '__main__':
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.remove(5)
    list.print()
