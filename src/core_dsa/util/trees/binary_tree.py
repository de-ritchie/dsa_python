from typing import List

from src.core_dsa.util.trees.node import BinaryTreeNode, T

# Level order build
def build_binary_tree(arr: List[T]) -> BinaryTreeNode[T]:
    
    n = len(arr)

    if n == 0:
        return None

    i = 0
    root: BinaryTreeNode[T] = BinaryTreeNode(arr[i])
    queue: List[BinaryTreeNode[T]] = []
    queue.append(root)

    while len(queue) > 0:
        
        node = queue.pop(0)

        if i + 1 < n and not arr[i + 1] is None:
            left = BinaryTreeNode(arr[i + 1])
            node.left = left
            queue.append(left)
        if i + 2 < n and not arr[i + 2] is None:
            right = BinaryTreeNode(arr[i + 2])
            node.right = right
            queue.append(right)
        
        i += 2
    
    return root

def level_order_traversal(root: BinaryTreeNode[T]):

    result = []

    if root is None:
        return result

    tmp = []
    queue: List[BinaryTreeNode[T]] = []

    queue.append(root)
    queue.append(None)

    while len(queue) > 0:

        node = queue.pop(0)

        if node is None:
            # Next level
            result.append(tmp)
            tmp = []
            if len(queue) > 0:
                queue.append(None)
            continue
        
        else:
            tmp.append(node.value)
            if not node.left is None:
                queue.append(node.left)
            
            if not node.right is None:
                queue.append(node.right)
    
    return result
