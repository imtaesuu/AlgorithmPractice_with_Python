import sys, datetime , math, itertools, random
from collections import Counter, defaultdict, deque
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 3 6 5 4 8 7 1 2
# 5 6 8 4 3 1 2 7

# 3 2 1 4
# 2 3 4 1

def to_postorder(p_start, p_end, i_start, i_end):    
    if p_end < p_start or i_end < i_start:
        return 
    
    root = preorder[p_start]
    pos = position[root]
    length = pos - i_start
    
    to_postorder(p_start+1, p_start+length, i_start, pos-1)
    to_postorder(p_start+length+1, p_end, pos+1, i_end)
    
    print(root, end = ' ')

T = int(input())
for _ in range(T):
    N = int(input())

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    position = [0] * (N+1)

    for i in range(N):
        position[inorder[i]] = i
    
    to_postorder(0, N-1, 0, N-1)
    print()


# 1. 전위에서 root를 찾음
# 2. 중위에서 root의 인덱스를 찾아서 왼쪽 오른쪽을 구별
# 3. 왼쪽 루트를 찾아서 왼쪽 꺼 재귀 보내고, 오른쪽 루트 찾아서 오른쪽거 재귀 보냄


    

    
    

    
    
    
    
    