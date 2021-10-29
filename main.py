import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [-1] * 100001
visited[N] = 0

q = deque()
q.append(N)

while q:
    x = q.popleft()
    print(x)
    
    if x == K:
        print(visited[x])
        break
    
    if x * 2 <= 100000 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.append(x*2)
    
    if x + 1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
    
    if x - 1 >= 0 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
        
    
