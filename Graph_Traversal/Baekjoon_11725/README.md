## - Baekjoon 11725 트리의 부모 찾기 문제 - [Link](https://www.acmicpc.net/problem/11725)
● 입력  
> 7  
1 6  
6 3  
3 5  
4 1  
2 4  
4 7

● 출력
> 4  
6  
1  
3  
1  
4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_11725/Baekjoon_11725.py)

```python
import sys

def input():
  return sys.stdin.readline().rstrip()

node = int(input())
graph = {key + 1 : [] for key in range(node)}
res = [0 for _ in range(node)]

for _ in range(node - 1):
  node1, node2 = map(int, input().split())
  if node1 not in graph[node2]:
    graph[node1] += [node2]
    graph[node2] += [node1]

def dps():
  arrived = [0]*(node+1)
  stack = [1]

  while stack:
    key = stack.pop()
    if not arrived[key]:
      arrived[key] = 1
      for val in graph[key]:
        stack.append(val)
        if res[val - 1] == 0:
          res[val - 1] = key
  
dps()
for child in res[1:]: print(child)
	
##### My code #####
##### Runtime 520ms, Memory 55996KB #####
```

## - **How To Solve**
- **in** 연산자에 대해 다시 한번 생각하게 해주는 문제
- **list**에서 **in**은 **O(n)** 의 시간복잡도를 가지기 때문에 자칫 사용하면 타임아웃이다.
- 시간초과만 아니면 그렇게 어렵지 않은 문제