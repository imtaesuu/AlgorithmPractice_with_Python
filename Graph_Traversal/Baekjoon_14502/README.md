## - Baekjoon 14502 연구소 문제 - [Link](https://www.acmicpc.net/problem/14502)
● 입력  
> 7 7  
2 0 0 0 1 1 0  
0 0 1 0 1 2 0  
0 1 1 0 1 0 0  
0 1 0 0 0 0 0  
0 0 0 0 0 1 1  
0 1 0 0 0 0 0  
0 1 0 0 0 0 0

● 출력
> 27

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_14502/Baekjoon_14502.py)

```python
import sys, copy, itertools
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
empty, queue = [], deque()
res, graph = 0, []
        
def bfs(table, q):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   
    while q:
        x, y = q.popleft()
        table[x][y] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and table[nx][ny] == 0:
                q.append((nx, ny))
                table[nx][ny] = -1
    cnt = 0
    for i in table:
        for j in i:
            if j == 0:
                cnt += 1
    return cnt
    
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 2:
            queue.append((i, j))
        elif graph[i][j] == 0:
            empty.append((i, j))   
    
case = list(itertools.combinations(empty, 3))
for l in case:
    table, q = copy.deepcopy(graph), copy.deepcopy(queue)
    for x, y in l:
        table[x][y] = 1  
    res = max(res, bfs(table, q))
print(res)
	
##### My code #####
##### Runtime 4912ms, Memory 34320KB #####
```

## - **How To Solve**
- 월요일에 적자