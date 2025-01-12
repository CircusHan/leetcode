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

from typing import List
def merge_two_lists(list1 : List[int], list2: List[int]) -> List[int]:
    (i, j) = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else :
            result.append(list2[j])
            j += 1
    if i >= len(list1):
        result += (list2[j:])
    else :
        result += (list1[i:])
    return result

def rmerge_two_lists(list1: List[int], list2: List[int]) -> List[int]:
    # 만약 list1이 비어 있으면 list2를 그대로 반환
    if len(list1) == 0:
        return list2
    # 만약 list2가 비어 있으면 list1을 그대로 반환
    elif len(list2) == 0:
        return list1

    # 두 리스트 모두 요소가 있을 경우,
    # 각각의 첫 번째 원소를 비교하여 더 작은 쪽을 결과 리스트에 이어 붙이고,
    # 해당 리스트는 한 칸 전진하여 재귀 호출
    if list1[0] <= list2[0]:
        return [list1[0]] + rmerge_two_lists(list1[1:], list2)
    else:
        return [list2[0]] + rmerge_two_lists(list1, list2[1:])


list1 = []
list2 = []
print(rmerge_two_lists(list1, list2))
list1 = [1,2,4]
list2 = [1,3,4]
print(rmerge_two_lists(list1, list2))
list1 = []
list2 = [0]
print(rmerge_two_lists(list1, list2))



