import sys, math
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
circles = [list(map(int, input().split())) + [0] for _ in range(N)]
circles.sort(key=lambda x:x[2])
circles.append([0, 0, sys.maxsize, 0])
graph = {i : [] for i in range(N+1)}

def distinguish_circle(c1, c2, idx):
    distance = math.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)
    #작은원이 큰원 내부에 존재하는 경우
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
    for j in range(N):
        if i != j and not check[i][j]:
            check[i][j], check[j][i] = True, True
            distinguish_circle(circles[i], circles[j], (i, j))
    if not circles[i][3]:
        graph[i].append(N)
        graph[N].append(i)
            

distance1 = bfs(N)
distance2 = bfs(distance1.index(max(distance1)))
    
# check = [[0]*(N+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i != j and not check[i][j]:
#             check[i][j], check[j][i] = True, True
#             res = max(res, bfs(i, j))
    
           
print(circles, graph, sep = '\n')
print(max(distance2))


#  3
#  5
# 2 0
#   1 4


