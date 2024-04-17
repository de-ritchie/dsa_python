"""
Reverse a Linked List

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Ref: https://leetcode.com/problems/reverse-linked-list/description/
"""

def reverse_recurs(head):

    # Base case
    if head is None or head.next is None:
        return head
    
    # Recursive case
    nxt = reverse_recurs(head.next)
    tmp = head.next
    head.next = tmp.next
    tmp.next = head

    return nxt

def reverse_iter(head):

    prev = None
    curr = head

    while not curr is None:
        
        tmp = curr.next
        curr.next = prev

        prev = curr
        curr = tmp
    
    return prev