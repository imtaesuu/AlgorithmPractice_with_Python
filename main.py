import sys, datetime , math, itertools, random
from collections import Counter, defaultdict, deque
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


#      1
#    2   3
#  4  5
#       
# 4 2 5 1 3  
# 4 5 2 3 1
# 1 2 4 5 3

# inorder     5 6 8 4 3 1 2 7
# postorder   5 8 4 6 2 1 7 3
# 3 6 5 4 8 7 1 2 

in_point = [0]*(N+1)
for i in range(N):
    in_point[inorder[i]] = i

def to_preorder(in_start, in_end, po_start, po_end):
    if in_start > in_end or po_start > po_end:
        return
    
    root = postorder[po_end]
    print(root, end = ' ')
    
    left = in_point[root] - in_start
    right = in_end - in_point[root]
    
    to_preorder(in_start, in_start + left - 1 , po_start, po_start + left - 1)
    to_preorder(in_end - right + 1, in_end, po_end - right, po_end - 1)
    
to_preorder(0,N-1,0,N-1)
        
    

    
    

    
    
    
    
    