import sys
from collections import deque
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()


def team_set(first, visited, graph):
    res = []
    stack = [(first, graph[first])]
    while stack:
        node = stack.pop()
        visited[node[0]] = True
        res.extend([node[0], node[1]])
        if not visited[node[1]]:
            stack.append((node[1], graph[node[1]]))
    while res:
        if res[0] == res[len(res)-1]: return res
        else: del res[0:2]
    return res
        
T = int(input())
for _ in range(T):
    team = set([])
    n = int(input())
    nums = list(map(int, input().split()))  
    graph = {i+1 : nums[i] for i in range(len(nums))}
    
    visited = [False]*(n+1)
    for slt in graph.keys():
        if not visited[slt]:
            team.update(team_set(slt, visited, graph))
    print(n-len(team))