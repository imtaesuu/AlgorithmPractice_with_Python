## - Baekjoon 16932 모양 만들기 문제 - [Link](https://www.acmicpc.net/problem/16932)
● 입력  
> 5 4  
1 1 0 0  
1 0 1 0  
1 0 1 0  
0 1 1 0  
1 0 0 1

● 출력
> 10

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_16932/Baekjoon_16932.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph, zero = [], []
move = [(-1 ,0), (1, 0), (0, -1), (0, 1)]
group = [[[0]*2 for _ in range(M)] for _ in range(N)]

# 0의 좌표를 리스트에 담아둠
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 0:
            zero.append((i, j))
           
# 그룹세팅 함수
def set_group(x, y, visited, g):
    q = deque([(x, y)])
    visited[x][y] = True
    tmp = [(x, y)]
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for n in move:
            nx, ny = x + n[0], y + n[1]    
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                tmp.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
                
    for i, j in tmp: 
        group[i][j][0] = g
        group[i][j][1] = cnt

# 순회하며 1을 발견할 때마다 미리 지점마다의 연결된 노드의 개수와 그룹을 세팅
visited, g = [[False]*M for _ in range(N)], 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            g += 1
            visited[i][j] = True
            set_group(i, j, visited, g)

# 0의 좌표마다 1일 때를 가정하여 상하좌우로 중복없이 마주치는 그룹의 개수를 더하며 결과값 업데이트
res = 1
for x, y in zero:
    num, v_group = 1, []
    for n in move:
        nx, ny = x + n[0], y + n[1]   
        if 0<=nx<N and 0<=ny<M and group[nx][ny][0] not in v_group:
            v_group.append(group[nx][ny][0])
            num += group[nx][ny][1]
    res = max(res, num)
print(res)

##### My code #####
##### Runtime 3976ms, Memory 254516KB #####
```

## - **How To Solve**
- 분명히 맞았지만 시간초과로 틀린 맞왜틀 정석 문제
- 항상 정석적인 풀이가 안될 때는 시간과 메모리 사용을 줄일 효율적인 기법이나 아이디어를 생각해야함
- 기본적으로 다차원 배열을 이용하거나, 큐에 좌표값 이외에 값을 넣어 탐색하는 풀이방식을 전제하에 생각
- 여기서는 3차원 배열에 그래프에 존재하는 모든 1을 **bfs**를 이용하여 연결된 그룹과 개수를 미리 세팅
- 모든 0에 대하여 상하좌우로 중복없이 마주치는 그룹의 개수를 더하여 결과값 비교