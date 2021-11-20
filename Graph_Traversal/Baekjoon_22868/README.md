## - Baekjoon 22868 산책 (small) 문제 - [Link](https://www.acmicpc.net/problem/22868)
● 입력  
> 4 5  
1 2  
1 3  
2 3  
2 4  
3 4  
1 4

● 출력
> 4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_22868/Baekjoon_22868.py)

```python
import sys
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    p, c = map(int, input().split())
    if c not in graph[p]:
        graph[p] += [c]
        graph[c] += [p]
S, E = map(int, input().split())

for k in graph.keys():
    graph[k] = sorted(graph[k])

def bfs(node, visited, cnt, end):
    q = deque([(node, visited, cnt)])
    visited.append(node)
    while q:
        node, visited, cnt = q.popleft()
        for child in graph[node]:
            if child == end:
                return (visited[:], cnt + 1)
            if child not in visited:
                q.append((child, visited + [child] , cnt + 1))        

prev_v, prev_c = bfs(S, [], 0, E)
print(bfs(E, prev_v, prev_c, S)[1])

##### PyPy3 #####
##### Runtime 760ms, Memory 395404KB #####
```

## - **How To Solve**
- S -> E -> S 로 복귀하는데에 있어 중복없는 경로만을 이용해야하는 최단경로 구하는 문제
- 큐에 노드, 방문지점, 길이 값을 넣어서 **bfs** 돌리면 되는 간단한 문제
- 단, 시간단축 면에서 있어 많은 생각과 새로운 방법을 고안해야하는 문제
- 힙을 사용하는 방법부터 최단경로에 해당하는 정점만을 방문처리 하기 위해 리스트를 다시만드는 방법까지 다양함
- 문제를 맞는것도 중요하지만, 시간 단축을 위해 큐에 큰 값을 넣을 때 주의해야함을 깨닫게 해준 문제