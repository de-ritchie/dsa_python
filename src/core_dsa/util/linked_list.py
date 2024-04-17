class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):

    tmp = head
    while not tmp is None:
        print(tmp.val, end='->')
        tmp = tmp.next
    print('null')
    print('-'*50)

def array_to_linked_list(nums):
    
    head = None
    prev = None

    for num in nums:
        node = ListNode(val=num)
        if prev is None:
            head = node
        else:
            prev.next = node
        
        prev = node

    # print_linked_list(head)

    return head

def linked_list_to_array(head):

    arr = []
    tmp = head
    while not tmp is None:
        arr.append(tmp.val)
        tmp = tmp.next
    
    return arr