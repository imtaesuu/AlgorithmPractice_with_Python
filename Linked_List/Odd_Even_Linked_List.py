from Linked_List import ListNode

##### my code #####
##### Runtime 36ms, Memory 16.1MB #####
# class leetcode_328:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return head
#         odd, even = head, head.next

#         while head and head.next:
#             head.next, head = head.next.next, head.next
            
#         start = odd       
#         while start and start.next:
#             start = start.next
#         start.next = even
#         return odd

##### The answer in the book #####
##### Runtime 93ms, Memory 16.4MB #####
class leetcode_328:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
		
        odd, even = head, head.next
		even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
			odd, even = odd.next, even.next
			
		odd.next = even_head
		return head	