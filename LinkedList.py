class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(arr):
    head = ListNode(arr[0])
    current = head
    for i in arr[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

def list_to_reverse_linkedlist(arr):
    current = ListNode(arr[0])
    # current = head
    prev = None
    for i in arr[1:]:
        prev = current
        current = ListNode(i)
        current.next = prev
    return current

list1 = list_to_reverse_linkedlist([2, 1, 5])
while list1:
    print(list1.val)
    list1 = list1.next

