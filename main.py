import sys, math
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
circles = [list(map(int, input().split())) + [0] for _ in range(N)]
circles.sort(key=lambda x:x[2])
circles.append([0, 0, sys.maxsize, 0])
graph = {i : [] for i in range(N+1)}

def distinguish_circle(c1, c2, idx):
    if (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 < (c1[2]-c2[2])**2:
        graph[idx[0]].append(idx[1])
        graph[idx[1]].append(idx[0])
            

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
        distinguish_circle(circles[i], circles[j], (i, j))
        break


distance1 = bfs(N)
distance2 = bfs(distance1.index(max(distance1)))

    
           
print(circles, graph, sep = '\n')
print(max(distance2))


#  3
#  5
# 2 0
#   1 4


