import sys, datetime , math, itertools, random
from collections import Counter, defaultdict
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def find_node(node):
    res = [node]
    while tree[node] != 0:
        res.append(tree[node])
        node = tree[node]
    return res
                        
T = int(input())
for _ in range(T):    
    N = int(input())
    tree = [0]*(N+1)
    for _ in range(N-1):
        p, c = map(int, input().split())
        tree[c] = p
    
    n1, n2 = map(int, input().split())
    
    path1 = find_node(n1)
    path2 = set(find_node(n2))
    
    for i in path1:
        if i in path2:
            print(i)
            break
            
