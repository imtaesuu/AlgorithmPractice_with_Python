##### Python 3 #####
##### Runtime 492ms, Memory 54.3MB #####

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 최소한 next노드가 존재할 때만 재귀
        if not (head and head.next):
            return head
        
        # 일반적인 리스트가 아닌 연결리스트이기에 런너 기법을 십분 활용
        # fast가 먼저 도착하면 slow는 중간지점이기에 slow 전 노드(half노드)까지를 자름
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        
        # 나누어진 두 연결리스트를 재귀함수로 보내버림
        list1 = self.sortList(head)
        list2 = self.sortList(slow)
        
        # 리턴할 때 병합하고 정렬하여 리턴
        return self.mergeLists(list1, list2)
        
        
    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 입력받은 두 리스트가 None이 아닐 때 val값을 서로 비교함
        # list1의 val 값이 더 크다면 두 노드를 교환하는데 값이 아닌 노드를 교환하기 때문에 연결된 노드까지 따라옴
        # list2는 가만히 냅두고 list1의 다음값과 같이 재귀함수로 보냄
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeLists(list1.next, list2)
        
        # return 에서 or을 활용 list1이 None일 때는 list2값을 보냄
        return list1 or list2
    