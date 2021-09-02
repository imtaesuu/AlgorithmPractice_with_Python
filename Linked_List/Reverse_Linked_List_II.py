from Linked_List import ListNode

##### My code #####
##### Runtime 76ms, Memory 14.5MB #####

# def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#     if not head or not head.next:
#         return head

#     node = start = ListNode(None)
#     node.next = head

#     for _ in range(left - 1):
#         start = start.next
#     end = start.next

#     for _ in range(right - left):
#         temp, start.next, end.next = start.next, end.next, end.next.next
#         start.next.next = temp
#     return node.next

##### The answer in the book #####
##### Runtime 28ms, Memory 14.4MB #####

def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    node = start = ListNode(None)
    node.next = head

    for _ in range(left - 1):
        start = start.next
    end = start.next

    for _ in range(right - left):
        temp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = temp
    return node.next