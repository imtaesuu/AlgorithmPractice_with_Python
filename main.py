import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

nodes = []
while True:
    try:
        node = int(input())
    except:
        break
    nodes.append(node)

def pre_to_post(left, right):
    if left >= right:
        return
    
    root = nodes[left]
    
    if nodes[right-1] < root:
        pre_to_post(left+1, right)
        print(root)
        return
    
    idx = None
    for i in range(left+1, right):
        if root < nodes[i]:
            idx = i
            break
            
    if idx is None:
        idx = right
    pre_to_post(left+1, idx)
    pre_to_post(idx, right)
    print(root)
    
pre_to_post(0, len(nodes)) 


