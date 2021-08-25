from Linked_List import ListNode

class leetcode_328:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd, even = head, head.next

        while head and head.next:
            head.next, head = head.next.next, head.next
            
        start = odd       
        while start and start.next:
            start = start.next
        start.next = even
        return odd