## - Baekjoon 14940 쉬운 최단거리 문제 - [Link](https://www.acmicpc.net/problem/14940)
● 입력  
> 15 15  
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1  
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1  
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0  
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1

● 출력
> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14  
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15  
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16  
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17  
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18  
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19  
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21  
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22  
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24  
11 12 13 14 15 16 17 18 19 20 0 0 0 0 25  
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26  
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0  
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_14940/Baekjoon_14940.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()

def bfs(x, y):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]             
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 0 and not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                q.append((nx, ny))
     
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if graph[i][j] == 2:
                visited[i][j] = 1
                graph[i][j] = 0
                q.append((i, j))
                bfs(i, j)
            elif graph[i][j] == 1:
                graph[i][j] = -1

for i in range(n):
    print(' '.join(map(str, graph[i])))
	
##### My code #####
##### Runtime 720ms, Memory 40216KB #####
```

## - **How To Solve**
- **bfs**를 이용하는 최단거리 문제, 진짜 간단한 문제이다.
- 단, 시간제한이 굉장히 빡빡하다. 
- 한번의 for문에 끝내야 하기 때문에 bfs는 2일 때 한번만 돌리게 하였다.
- q를 한번만 만들었는가, visited를 제한적으로 사용하였는가, dx dy를 한번만 만들었는가 등
- 코드 최적화에 최대한 신경써야 풀리는 문제였다.