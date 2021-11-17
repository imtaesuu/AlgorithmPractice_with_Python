import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000)

n = int(input())
tree = {i+1 : [] for i in range(n)}
res = 0

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    if parent not in tree[child]:
        tree[parent] += [(child, weight)]
        tree[child] += [(parent, weight)]

# def dfs(node, visited, length):
#     global res
#     if node not in visited:
#         visited.append(node)
#         for val in tree[node]:
#             length += val[1]
#             dfs(val[0], visited, length)
#             length -= val[1]
#         res = max(res, length)


# 1: [(2, 3), (3, 2)], 2: [(1, 3), (5, 8), (4, 9)], 3: [(1, 2)], 4: [(2, 9)], 5: [(2, 8)]}

def dfs(node, visited):
    global res
    stack = [(node, 0)]
    length = 0
    
    while stack:
        node, dstc = stack.pop()
        if not visited[node]:
            visited[node] = True
            
            
            for val in tree[node]:
                if visited[val[0]]:
                    res = max(res, dstc)
                    continue
                stack.append((val[0], val[1] + dstc))
                                   
                    
for i in range(n):
    visited = [False]*(n+1)
    dfs(i+1, visited)
    
print(res)
    