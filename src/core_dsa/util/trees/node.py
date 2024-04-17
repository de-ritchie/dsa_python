from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T = None) -> None:
        self.value: T = value

class BinaryTreeNode(Node[T]):
    def __init__(self, value: T = None) -> None:
        super().__init__(value)
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None