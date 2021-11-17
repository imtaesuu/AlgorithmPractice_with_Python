##### My code #####
##### Runtime 5876ms, Memory 226640KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
tree = {i+1 : [] for i in range(n)}
res = 0
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    if parent not in tree[child]:
        tree[parent] += [(child, weight)]
        tree[child] += [(parent, weight)]

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