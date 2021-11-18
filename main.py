import sys
from collections import deque
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()


[(2, 1), (1, 3), (3, 3)]

def team_set(node):
    visited = [False]*(len(graph)+1)
    visited[node] = True
    res = [node]
    stack = [node]
    while stack:
        node = stack.pop()
        res.append(graph[node])
        if not visited[graph[node]]:
            visited[graph[node]] = True
            stack.append(graph[node])
    if res[0] == res[len(res)-1]:
        return res
    else: return []
        
T = int(input())

for _ in range(T):
    team = set([])
    n = int(input())
    nums = list(map(int, input().split()))  
    v = [False]*(n+1)
    graph = {i+1 : nums[i] for i in range(len(nums))}
    
    for i in range(1, n+1):
        if not v[i]:
            tmp = team_set(i)
            team.update(tmp)
            for j in tmp:
                v[j] = True
        

    print(n-len(team))
            

    
            
    