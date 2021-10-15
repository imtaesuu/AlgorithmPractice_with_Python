## - Baekjoon 1260 DFS와 BFS 문제 - [Link](https://www.acmicpc.net/problem/1260)
● 입력  
> 5 5 3  
5 4  
5 2  
1 2  
3 4  
3 1

● 출력
> 3 1 2 5 4  
3 1 4 2 5  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_1260/Baekjoon_1260.py)

```python
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

node, line, start = map(int, input().split())
graph = {key + 1 : [] for key in range(node)}

for _ in range(line):
  node1, node2 = map(int, input().split())
  if node1 not in graph[node2]:
    graph[node1] += [node2]
    graph[node2] += [node1]

def dfs():
  arrived = []
  stack = [start]
  table = {key : list(reversed(sorted(val))) for key, val in graph.items()}

  while stack:
    key = stack.pop()
    if key not in arrived:
      arrived.append(key)
      for val in table[key]:
        stack.append(val)
  return arrived

def bfs():
  arrived = [start]
  queue = deque([start])
  table = {key : list(sorted(val)) for key, val in graph.items()}

  while queue:
    key = queue.popleft()
    for val in table[key]:
      if val not in arrived:
        arrived.append(val)
        queue.append(val)
  return arrived

print(*dfs())
print(*bfs())
	
##### My code #####
##### Runtime 324ms, Memory 32684KB #####
```

## - **How To Solve**
- 방문할 수 있는 정점이 여러개 있을 때 정점 번호가 작은 것을 먼저 방문하는 조건이 붙은 문제
- 일반적인 **dfs**와 **bfs**에서 따로 **table**을 만들어 dic의 val값을 정렬해준다.
- **dfs**는 정렬 후 뒤집어주고 **bfs**는 정렬만 해주는 게 포인트다.