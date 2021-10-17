## - Baekjoon 1325 효율적인 해킹 문제 - [Link](https://www.acmicpc.net/problem/1325)
● 입력  
> 5 4  
3 1  
3 2  
4 3  
5 3

● 출력
> 1 2

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_1325/Baekjoon_1325.py)

```python
import sys
from collections import deque

def input():
  return sys.stdin.readline()

cmt, line = map(int, input().split())
graph = {key + 1 : [] for key in range(cmt)}

for _ in range(line):
  node1, node2 = map(int, input().split())
  graph[node2] += [node1]

def bfs(start):
  arrived = [0] * (cmt + 1)
  arrived[start] = 1 
  q = deque([start])
  cnt = 0

  while q:
    temp = q.popleft()
    for node in graph[temp]:
      if not arrived[node]:
        q.append(node)
        arrived[node] = 1
        cnt += 1
  return cnt

max_num = 0
res = []
for i in range(cmt):
  if graph[i + 1]:
    num = bfs(i + 1)
    if max_num <= num:
      if max_num < num:
        res.clear()
      max_num = num
      res.append(i + 1)
print(*res)
	
##### My code #####
##### Runtime 14020ms, Memory 226228KB #####
```

## - **How To Solve**
- 문제 자체는 전혀 어렵지 않았지만 파이썬의 속도를 체감 시켜줬던 문제
- pypy3로 제출해야 시간초과 나지 않고 정상적으로 작동한다.
- 자기자신을 제외하고 카운팅하기 위해 **bfs**를 사용했다.
- 일반적인 **bfs**에 카운팅을 추가했고 가장 많이 자식을 가지고 있는 것을 for문으로 추려냈다.