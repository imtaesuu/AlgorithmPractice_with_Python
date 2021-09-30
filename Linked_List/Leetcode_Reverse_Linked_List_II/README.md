# - Leetcode 92. Reverse Linked List II - [Link](https://leetcode.com/problems/reverse-linked-list-ii/)
● 입력  
> 1 → 2 → 3 → 4 → 5 → NULL, left = 2, right = 4

● 출력
> 1 → 4 → 3 → 2 → 5 → NULL


# - 내가 접근했던 방식과 풀이 - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Linked_List/Reverse_Linked_List_II.py)
__인덱스__ 가 주어지면, __인덱스__ 에 해당되는 구역만 __역순__ 으로 재구성하는 문제이다. 구역이 시작되는 지점의 노드와 시작되기 전의 노드를 사용하여 
문제를 해결하려고 하였다.

```python
if not head or not head.next:
	return head
```  
먼저 입력값과, 노드의 다음값이 없을 때는 값을 그대로 리턴했고

```python
node = start = ListNode(None)
node.next = head
``` 
결과값을 리턴할 최종 노드와 시작지점을 나타내는 노드를 __None__ 으로만든후, __head__ 를 __None__ 다음으로 연결시켰다.  
__head__ 를 __None__ 다음으로 연결시킴으로,  __left__ 가 1일 때와 그 이상일 때의 코드를 구분하지 않고 한 번에 해결할 수 있게 작성할 수 있다.

```python
for _ in range(left - 1):
	start = start.next
end = start.next
``` 
구역이 시작되는 지점의 노드와 시작되기 전의 노드를 사용하여 문제를 해결하기 위해, __start__ 와 __end__ 를 지정하고

```python
for _ in range(right - left):
	temp, start.next, end.next = start.next, end.next, end.next.next
	start.next.next = temp
return node.next
``` 
__end.next__ 즉 __end__ 의 __next__ 노드에 그 앞의 노드를 이어주기 위해 임시 포인터 __temp__ 를 만들어주고, __start__ 의 __next__ 에는  
__end__ 의 __next__ 노드를, __end__ 의 __next__ 에는 __end__ 의 __next.next__ 노드를 연결시켜 준뒤, __start__ 의 __next__ 노드를 할당받은 __temp__ 를  
__start__ 의 __next.next__ 에 연결시켜줌으로써 역순으로 노드를 재구성하고, __None__ 다음 노드인 __node.next__ 를 반환한다. 전체 코드는 아래와 같다.

```python
def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if not head or not head.next:
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

##### Runtime 76ms, Memory 14.5MB #####
``` 


# - 참고한 다른풀이
```python
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

##### Runtime 28ms, Memory 14.4MB #####
```
인덱스 값인 __left__ 와 __right__ 의 같을 때의 예외 상황을 처리하는 코드의 차이 때문에 속도의 차이가 벌어질 줄은 몰랐다.  
단지 __int__ 값인 __left__ 와 __right__ 의 동일 여부를 확인하는 것이 노드의 __next__ 를 확인하는 것보다 훨씬 빠르다는 것을 알았다.   
앞으로는 단순한 상황처리에서도 코드 최적화를 신경쓰고 작성해야겠다.


