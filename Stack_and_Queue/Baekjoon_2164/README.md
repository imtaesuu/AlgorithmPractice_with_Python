## - Baekjoon 2164 카드 소거 문제 - [Link](https://www.acmicpc.net/problem/18258)
● 입력  
> 6

● 출력
> 4
## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_2164/Baekjoon_2164.py)

```python
from collections import deque

num = int(input())

stack = deque([x+1 for x in reversed(range(num))])

while len(stack) != 1:
  stack.pop()
  stack.appendleft(stack.pop())

print(stack[0])
	
##### My code #####
##### Runtime 288ms, Memory 54852KB #####
```

## - **How To Solve**
- **데크**를 이용하여 간단하게 풀 수 있는 문제이다.
- 변수명을 **stack**으로 하였고 카드를 뒤집는 상황에서 리스트를 뒤집었는데 사실 그렇게 하지 않아도 풀 수 있다.
