import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
    
input = sys.stdin.readline

K = int(input())
nodes = list(input().split())
res = [[] for _ in range(K)]

def make_tree(elements, level):
    mid = int(len(elements)/2)
    res[level].append(elements[mid])
    
    if mid == 0:
        return
    
    make_tree(elements[:mid], level+1)
    make_tree(elements[mid+1:], level+1)

make_tree(nodes, 0)

for i in res:
    print(' '.join(i))