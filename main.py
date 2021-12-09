import sys, math, itertools
from collections import Counter, defaultdict
import heapq
    
input = sys.stdin.readline

maxh, minh = [], []
solved = defaultdict(int)

heapq.heapify


for _ in range(int(input())):
    P, L = map(int, input().split())
    heapq.heappush(maxh, (-L, -P))
    heapq.heappush(minh, (L, P))

M = int(input())
for _ in range(M):
    cmd = input().split()
    P = int(cmd[1])
    if cmd[0] == 'add':
        solved[P] = 0
        L = int(cmd[2])
        heapq.heappush(maxh, (-L, -P))
        heapq.heappush(minh, (L, P))
    elif cmd[0] == 'solved':
        solved[P] = 1
    else:
        while heap and solved[-maxh[0][1]]:
            heapq.heappop(maxh)
        while heap and solved[minh[0][1]]:
            heapq.heappop(minh)
        
        if P == 1 and maxh:
            print(-maxh[0][1])
        elif P == -1 and minh:
            print(minh[0][1])
