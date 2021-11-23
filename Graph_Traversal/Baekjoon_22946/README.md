## - Baekjoon 22946 원 이동하기 1 문제 - [Link](https://www.acmicpc.net/problem/22946)
● 입력  
> 8  
8 8 7  
10 6 4  
4 5 1  
1 0 1  
6 7 10  
3 9 1  
10 6 1  
-1 7 1  

● 출력
> 4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_22946/Baekjoon_22946.py)

```python
import sys, math
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
circles = [list(map(int, input().split())) + [0] for _ in range(N)]
circles.sort(key=lambda x:x[2])
circles.append([0, 0, 15000000, 0])
graph = {i : [] for i in range(N+1)}

def distinguish_circle(c1, c2, idx):
    distance = math.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)
    if (c2[2] - c1[2] > distance) or (c1[0] == c2[0] and c1[1] == c2[1]):
        if not c1[3]:
            graph[idx[0]].append(idx[1])
            graph[idx[1]].append(idx[0])
            c1[3] = 1

def bfs(start):
    visited = [0]*(N+1)
    visited[start] = 1
    distance_list = [0 for _ in range(N+1)]
    q = deque([start])
    while q:
        node= q.popleft()    
        distance_list[node] = visited[node] - 1
        for c in graph[node]:
            if not visited[c]:
                visited[c] = visited[node] + 1
                q.append(c)
    return distance_list

check = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(i+1,N+1):
        if not check[i][j]:
            check[i][j], check[j][i] = True, True
            distinguish_circle(circles[i], circles[j], (i, j))
    if not circles[i][3]:
        graph[i].append(N)
        graph[N].append(i)
            
distance1 = bfs(N)
distance2 = bfs(distance1.index(max(distance1)))
print(max(distance2))

##### PyPy3 #####
##### Runtime 2304ms, Memory 783992KB #####
```

## - **How To Solve**
- 내 사고방식의 한계를 보여준 대표적인 문제, 단순한걸 복잡하게 구현하려고 한다.
- **dfs**나 **bfs**를 구현하는 것보다 트리 자체를 만드는 게 더 복잡한 문제이다.
- 좌표평면상의 원의 내부 공간에서의 이동을 구현해야 하기 때문에 생각이 많아진 문제이다.
- 또한 트리에서 가장 먼 거리를 구할 때는 트리의 지름 구하기 문제를 경험삼았다.
- 임의의 두 원이 포함되어있거나 포함하는 원이면 트리 경로에 추가했다.
- 좌표평면 자체도 반지름이 굉장히 큰 원으로 가정하여 트리 경로를 추가하였다.
- 원 이동하기 2 문제에서 조금더 효율적이고 시간 단축을 위한 풀이를 해봐야겠다.