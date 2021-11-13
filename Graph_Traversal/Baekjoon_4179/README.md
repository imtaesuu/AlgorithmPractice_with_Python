## - Baekjoon 4179 불! 문제 - [Link](https://www.acmicpc.net/problem/4179)
● 입력  
> 4 4  ('' 제외)  
'####'  
'#JF#'  
'#..#'  
'#..#'  

● 출력
> 3

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_4179/Baekjoon_4179.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
graph, J, F = [], [], []
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*C for _ in range(R)]

for i in range(R):
    graph.append(list(input()))
    for j in range(C):
        if graph[i][j] == 'J': J += [i, j]
        elif graph[i][j] == 'F': F.append((i, j))

def bfs():
    q = deque()
    q.append((J[0], J[1], 'J'))
    graph[J[0]][J[1]] = 1
    
    for i, j in F:
        q.append((i, j, 'F'))
        visited[i][j] = True
    
    while q:
        x, y, check = q.popleft()
        if check == 'J' and graph[x][y] != 'F':
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return graph[x][y]
        
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0<=nx<R and 0<=ny<C:
                if check == 'J' and graph[x][y] != 'F' and graph[nx][ny] == '.':
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny, 'J'))
                elif check == 'F' and graph[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = 'F'
                    q.append((nx, ny, 'F'))
    return 'IMPOSSIBLE'
print(bfs())

##### My code #####
##### Runtime 2636ms, Memory 48640KB #####
```

## - **How To Solve**
- 설명이 좀 성의 없는 문제?, 다국어 문제라서 그런가 너무 간단히 나와있었다.
- 처음 실패들은 거의다 불이 하나라고만 가정하고 풀었던 문제라 다 틀렸고 이것 때문에 굉장히 시간낭비 했다.
- 다른 풀이들 보면 큐를 두개 씩 만들어서 따로 **bfs** 돌렸지만, 어차피 지훈이 다음 불이 이동하기 때문에 한 큐로 돌려도 된다.
- visited는 불만 넣어주고, 지훈이는 어차피 숫자로 바뀌기 때문에 굳이 만들어줄 필요가 없다.
- 돌리는 중간에 check값이 J 즉 지훈이고 불에 닿지 않았으며 테두리 부분에 있다면 결과값을 리턴해줬다.