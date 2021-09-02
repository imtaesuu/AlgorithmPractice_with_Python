# AlgorithmPractice with Python
자료구조, 알고리즘 공부 With Python :memo::memo:  
Github와도 친해지고 자료구조 공부도 할겸 내 풀이와 다른 풀이를 비교하면서 생각해보고 정리하는 용도로 만들었다.  
대부분의 문제는 [파이썬 알고리즘 인터뷰](https://github.com/onlybooks/algorithm-interview)를 참고한 코드가 들어있다.


# Linked List 
## - Leetcode 328. Odd Even Linked List - [Link](https://leetcode.com/problems/odd-even-linked-list/)
● 입력  
> 1 → 2 → 3 → 4 → 5 → NULL  

● 출력
> 1 → 3 → 5 → 2 → 4 → NULL  

## - 내가 접근했던 방식과 풀이 - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/commit/bb853c64241844e3c8264586549233cacf12945f) 
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
변수 odd와 even에 head의 첫 자리와 그 다음 자리로 할당해주고, 입력받은 연결 리스트를 한칸 씩 땡겨주면서   
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
