##### PyPy3 #####
##### Runtime 760ms, Memory 395404KB #####

import sys
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    p, c = map(int, input().split())
    if c not in graph[p]:
        graph[p] += [c]
        graph[c] += [p]
S, E = map(int, input().split())

for k in graph.keys():
    graph[k] = sorted(graph[k])

def bfs(node, visited, cnt, end):
    q = deque([(node, visited, cnt)])
    visited.append(node)
    while q:
        node, visited, cnt = q.popleft()
        for child in graph[node]:
            if child == end:
                return (visited[:], cnt + 1)
            if child not in visited:
                q.append((child, visited + [child] , cnt + 1))        

prev_v, prev_c = bfs(S, [], 0, E)
print(bfs(E, prev_v, prev_c, S)[1])
