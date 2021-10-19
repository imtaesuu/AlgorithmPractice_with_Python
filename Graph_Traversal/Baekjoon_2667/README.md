## - Baekjoon 2667 단지 번호 붙이기 문제 - [Link](https://www.acmicpc.net/problem/2667)
● 입력  
> 7  
0110100  
0110101  
1110101  
0000111  
0100000  
0111110  
0111000

● 출력
> 3  
7  
8  
9

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2667/Baekjoon_2667.py)

```python
##### My code #####
##### Runtime 108ms, Memory 31900KB #####

import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

def dfs(x, y):
    if x < 0 or x >= N or \
        y < 0 or y >= N or \
        graph[x][y] == 0:
            return 0
    
    graph[x][y] = 0
    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
         
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] 
        cnt += dfs(nx, ny)    
    return cnt

res = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            res.append(dfs(x, y))
            
print(len(res))
print(*sorted(res), sep = '\n')
	
##### My code #####
##### Runtime 84ms, Memory 29820KB #####
```

## - **How To Solve**
- **bfs**나 **dfs** 중 아무거나 사용해도 풀리는 문제
- 입력받은 그래프의 값을 하나씩 순회하며, 이미 방문했더라면 0을 리턴
- 1을 만날때마다 카운팅 해주면서 풀이했다.