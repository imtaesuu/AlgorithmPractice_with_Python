# AlgorithmPractice with Python
자료구조, 알고리즘 공부 With Python :memo::memo:

## Linked List 
### - Leetcode 328. Odd Even Linked List 
'''python
def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
        return head
    odd, even = head, head.next

    while head and head.next:
        head.next, head = head.next.next, head.next
            
        odd_tail = odd       
        while odd_tail and odd_tail.next:
            odd_tail = odd_tail.next
        odd_tail.next = even
        return odd
'''