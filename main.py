import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

parents = list(map(int, input().split()))
del_node = int(input())

graph = [set() for _ in range(N)]

for idx in range(N):
    if parents[idx] == -1:
        root = idx
    else:
        graph[parents[idx]].add(idx)
    
def dfs(node):
    if len(graph[node]) == 0:
        return 1
    
    res = 0
    for n in graph[node]:
        res += dfs(n)
    
    return res
    
if parents[del_node] != -1:
    graph[parents[del_node]].remove(del_node)
    print(dfs(root))
else:
    print(0)
