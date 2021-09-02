# AlgorithmPractice with Python
자료구조, 알고리즘 공부 With Python :memo::memo:  
__Github__ 와 친해지고 __자료구조__ 공부도 할겸 내 풀이와 다른 풀이를 비교하면서 생각해보고 정리하는 용도로 만들었다.  
대부분의 문제는 [파이썬 알고리즘 인터뷰](https://github.com/onlybooks/algorithm-interview)를 참고한 코드가 들어있다.


# Linked List 
## - Leetcode 328. Odd Even Linked List - [Link](https://leetcode.com/problems/odd-even-linked-list/)
● 입력  
> 1 → 2 → 3 → 4 → 5 → NULL  

● 출력
> 1 → 3 → 5 → 2 → 4 → NULL  

## - 내가 접근했던 방식과 풀이 - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Linked_List/Odd_Even_Linked_List.py) 
연결 리스트를 __홀수번째(index. 1, 3, 5 …)__ 노드 다음에 __짝수번째(index. 2, 4, 6 …)__ 노드가 오도록 재구성하는 문제이다.  
문제에서는 __공간 복잡도 O(1), 시간 복잡도 O(n)__ 을 요구하고 있다. 최대한 변수를 적게 사용하려는 기준을 세우고 접근했다.

```python
if head is None:
    return head
```  
먼저 입력값이 없을 때, 그대로 값을 리턴했고  

```python
odd, even = head, head.next
while head and head.next:
    head.next, head = head.next.next, head.next
```
변수 __odd__ 와 __even__ 에 __head__ 의 첫 자리와 그 다음 자리로 할당해주고, 입력받은 연결 리스트를 한칸 씩 땡겨주면서   
현재 자리로부터 그 2칸 뒤의 값을 연결시킴으로서 홀수번째 노드끼리, 또 짝수번째 노드끼리 연결시킨 다음

```python
odd_tail = odd       
while odd_tail and odd_tail.next:
    odd_tail = odd_tail.next
        
odd_tail.next = even
return odd
```

홀수번째 노드로 이루어진 연결 리스트의 끝부분을 얻은 후, 짝수번째 노드로 이루어진 연결 리스트의 첫 부분을  
연결시켜줌으로써 요구 사항을 적절히 충족시킨 채로 코드를 작성해 보았다. 전체 코드는 아래와 같다.

```python
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
	
##### Runtime 36ms, Memory 16.1MB #####
```  
  
## - 참고한 다른풀이
```python
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

##### Runtime 93ms, Memory 16.4MB #####
```
  
앞부분은 똑같지만 내 풀이처럼 __while__을 여러번 쓰지 않고 한번에 해결하기 위해서 odd와 even을 한칸씩 땡기면서 연결시켰다.   
나는 __odd의 끝부분__ 을 사용했지만 여기서는 __even의 첫부분__ 을 사용했다. 이 방식이 코드는 더 깔끔하고 이해하기 쉬워보인다.  
하지만 leetcode에서 테스트한 결과 내 풀이가 속도도 빠르고 메모리도 적게 들었다.   

## - Leetcode 92. Reverse Linked List II - [Link](https://leetcode.com/problems/reverse-linked-list-ii/)
● 입력  
> 1 → 2 → 3 → 4 → 5 → NULL, left = 2, right = 4

● 출력
> 1 → 4 → 3 → 2 → 5 → NULL


## - 내가 접근했던 방식과 풀이 - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Linked_List/Reverse_Linked_List_II.py)
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
__head__ 를 __None__ 다음으로 연결시킴으로,  __left__ 가 1일 때와 그 이상일 때의 코드를 구분하지 않고 한 번에  
해결할 수 있게 작성할 수 있다.

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


## - 참고한 다른풀이
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


