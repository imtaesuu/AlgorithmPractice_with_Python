import sys, datetime , math, itertools, random
from collections import Counter, defaultdict, deque
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find_parents(node):
    for parents, child in tree.items():
        if node in child:
            return parents
    return 0

while True:
    N, K = map(int, input().split())
    if not N+K:
        break
    
    elements = list(map(int, input().split()))
    tree = defaultdict(set)
    
    parents = deque([elements[0]])
    root = prev = parents[0]
    parent = 0
    grand_parent = 0
    
    for e in elements[1:]:        
        if prev + 1 < e:
            parent = parents.popleft()
        
        parents.append(e)
        tree[parent].add(e)
        prev = e

    p1 = find_parents(K)
    if not p1:
        print(0)
        continue
    
    p2 = find_parents(p1)    
    if not p2:
        print(0)
        continue

    res = 0
    for t in tree[p2]:
        if t != p1:
            res += len(tree[t])
    
    print(res)
            