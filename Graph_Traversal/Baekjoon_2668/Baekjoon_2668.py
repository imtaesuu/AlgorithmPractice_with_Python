##### My code #####
##### Runtime 92ms, Memory 31848KB #####

import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
graph, res = {}, set()
for i in range(1, N+1): graph[i] = int(input())

def dfs(node):
    stack = [node]
    a_set, b_set = set(), set()
    a_set.add(node)
    visited = [node]   
    while stack:
        node = stack.pop()    
        b_set.add(graph[node]) 
    
        if graph[node] not in visited:
            stack.append(graph[node])
            a_set.add(graph[node])
            visited.append(graph[node])
    
    if a_set == b_set:
        return a_set
    return {}

for key in graph: res.update(dfs(key))
res = sorted(res)
print(len(res), *res, sep = '\n')