import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(root):
    stack = [root]
    visited = set([root])
    
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if n in visited:
                return False
            stack.append(n)
            visited.add(n)
    return True

num = 0
while True:
    graph = defaultdict(list)
    nodes, childs = set(), set()
    num += 1
    
    run = True
    while run:
        elements = list(map(int, input().split()))
        
        if len(elements) == 0:
            continue
        
        if elements[0] == -1 and elements[1] == -1:
            sys.exit(0)
            
        
        nodes.update(elements)
        
        for i in range(0, len(elements), 2):
            if elements[i] == 0 and elements[i+1] == 0:
                run = False
                break
            graph[elements[i]].append(elements[i+1])
            childs.add(elements[i+1])
    
    if len(graph) == 0:
        print(f'Case {num} is a tree.')
        continue
    

    root = nodes - childs
    root.remove(0)

    if len(root) != 1:
        print(f'Case {num} is not a tree.')
        continue
    
    
    print(f'Case {num} is a tree.' if dfs(root.pop()) else f'Case {num} is not a tree.')
        
