##### PyPy3 #####
##### Runtime 1444ms, Memory 246048KB #####

import sys
input = lambda : sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))    
    visited = [False]*(n+1)
    
    res = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        first = i
        link = [first]
        visited[first] = True
        
        while True:
            tmp = graph[first]
            if visited[tmp]:
                break
            first = tmp
            link.append(first)
            visited[first] = True
        
        if link and tmp in link:
            res += len(link[link.index(tmp):])
    print(n- res)