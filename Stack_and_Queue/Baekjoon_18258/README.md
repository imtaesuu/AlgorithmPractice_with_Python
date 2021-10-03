## - Baekjoon 18258 큐 구현 문제 - [Link](https://www.acmicpc.net/problem/18258)
● 입력  
> 15  
push 1  
push 2  
front  
back  
size  
empty  
pop  
pop  
pop  
size  
empty  
pop  
push 3  
empty  
front

● 출력
>1  
2  
2  
0  
1  
2  
-1  
0  
1  
-1  
0  
3

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_18258/Baekjoon_18258.py)

```python
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

cnt = int(input())
queue = deque()

for _ in range(cnt):
  cmd = input().split()

  if cmd[0] == 'push':
    queue.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(queue))
  elif cmd[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif cmd[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif cmd[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])
	
##### My code #####
##### Runtime 2184ms, Memory 92888KB #####
```

## - **How To Solve**
- 기본적인 구현 문제이며, **큐**의 구조를 이해하고 있으면 구현하기 쉽다.
- **데크**의 **popleft**를 사용하여 **O(1)** 의 속도로 구현되게 끔 풀이하였다.