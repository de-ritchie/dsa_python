from typing import List

from src.core_dsa.util.trees.node import BinaryTreeNode, T

def sorted_array_to_bst(arr: List[T]) -> BinaryTreeNode[T]:

    n = len(arr)

    if n == 0:
        return None
    
    mid = (n - 1)//2

    node = BinaryTreeNode(arr[mid])
    left = sorted_array_to_bst(arr[:mid])
    right = sorted_array_to_bst(arr[mid + 1:])

    node.left = left
    node.right = right

    return node