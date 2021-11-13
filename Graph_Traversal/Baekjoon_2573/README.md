## - Baekjoon 2573 빙산 문제 - [Link](https://www.acmicpc.net/problem/2573)
● 입력  
> 5 7  
0 0 0 0 0 0 0  
0 2 4 5 3 0 0  
0 3 0 2 5 2 0  
0 7 6 2 4 0 0  
0 0 0 0 0 0 0

● 출력
> 2

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2573/Baekjoon_2573.py)

```python
import sys
from collections import deque
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, visited, graph):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()   
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] != 0: 
                    graph[nx][ny] -= 1
                    if graph[nx][ny] <= 0:
                        visited[nx][ny] = True
                        graph[nx][ny] = 0

def dfs(x, y, visited):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            dfs(nx, ny, visited)
                  
t = 0
while True:
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and not visited[i][j]:
                bfs(i, j, visited, graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                dfs(i, j, visited)
                cnt += 1 
    t += 1
    if cnt >= 2:
        print(t)
        break
    elif cnt == 0:
        print(0)
        break

##### My code #####
##### Runtime 3620ms, Memory 462812KB #####
```

## - **How To Solve**
- 자칫 간단하다고 생각 할 수 있지만, 이미 녹아버린 빙산을 바로 옆 빙산이 물로 취급해 녹일 때 포함해버리는 과정을 조심해야함
- 첫 순회 때 **bfs**로 빙산을 녹여줬음, 녹다가 0 이되거나 0보다 작아져 버리면 방문 표시를 해둠으로 위 사태를 방지
- 두번째 순회 때 **dfs**로 빙산을 카운팅, 속도를 더 뽑고 싶으면 재귀말고 스택으로 구현해도 됨
- 더 속도를 뽑고 싶다면 테두리 부분을 range를 이용하여 카운팅 때 제외하면 됨
- 다른 방법으로는 그냥 **bfs** 하나만으로 빙산 주변 0을 카운팅해서 따로 큐에 담고 for문을 나온뒤 
- 빙산 카운팅 해준 뒤 동시에 저장해둔 큐를 이용하여 빙산 녹여주면 됨
- 생각보다 쉽지만 타임아웃을 걱정하면서 풀면 조금 돌아가게 풀 수도 있는 문제