## - Leetcode 147 Insertion Sort List - [Link](https://leetcode.com/problems/insertion-sort-list/)
● 입력  
> head = [-1,5,3,4,0]

● 출력
>  [-1,0,3,4,5]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Sort/Leetcode_56/Leetcode_56.py)

```python
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 현재 위치와 마지막 결과값을 리턴하기 위한 위치가 필요함
        # 또한 val값이 None이면 비교가 안되기 때문에 초기값으로 0으로 설정
        cur = root = ListNode(0)
        while head:
            # 현재 현재 위치값과 head의 값을 비교하여 head가 더 크다면 
            # 큰 수가 더 뒤로 배치되어야 하기 때문에 cur의 위치를 옮겨줌
            while cur.next and cur.next.val < head.val:
                cur = cur.next
        
            # 현재 위치는 head를 받아 따로 저장
            # head의 다음값을 cur.next로 받고
            # head는 다음칸으로 이동
            cur.next, head.next, head = head, cur.next, head.next
            
            # 만약 다음으로 확인할 값이 현재 위치값보다 작을경우에만 최적화를 위해
            # cur을 맨 앞인 초기 위치로 옮겨둠
            if head and cur.val > head.val:
                cur = root
        return root.next
        
##### Python 3 #####
##### Runtime 165ms, Memory 16.7MB #####
```

## - **How To Solve**
- 정확히는 삽입정렬이 아니지만 연결리스트임을 감안해 수를 맨앞에서부터 비교해야 함
