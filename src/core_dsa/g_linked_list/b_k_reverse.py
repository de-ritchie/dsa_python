"""
Reverse Node in K-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Ref: https://leetcode.com/problems/reverse-nodes-in-k-group/description/
"""

from src.core_dsa.g_linked_list.a_reverse_linked_list import reverse_iter

from src.core_dsa.util.linked_list import ListNode, print_linked_list

def reverse_k_group_recurs(head: ListNode, curr: ListNode, i: int, k: int) -> ListNode:
    
    # Base case
    if curr is None:
        return head
    
    i += 1

    if i == k:

        # Unlink next node
        tmp = curr.next
        curr.next = None

        # Reverse
        reverse_iter(head)
        print_linked_list(curr)

        # Recursive case
        sub_node = reverse_k_group_recurs(tmp, tmp, 0, k)

        # link next node
        head.next = sub_node

        return curr
    
    # Recursive case
    return reverse_k_group_recurs(head, curr.next, i, k)

def reverse_k_group(head, k):
    return reverse_k_group_recurs(head, head, 0, k)