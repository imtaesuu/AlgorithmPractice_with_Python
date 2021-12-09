##### PyPy3 #####
##### Runtime 348ms, Memory 153080KB #####

import sys, heapq    
input = sys.stdin.readline
maxh, minh = [], []
solved = set()

def rmv(heap):
    while heap and heap[0][1] in solved:
        heapq.heappop(heap)
        
N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(maxh, ((-L, -P), P))
    heapq.heappush(minh, ((L, P), P ))

M = int(input())
for _ in range(M):
    cmd = input().split()
    P = int(cmd[1])
    if cmd[0] == 'add':
        if P in solved:
            rmv(maxh)
            rmv(minh)
            solved.remove(P)
        L = int(cmd[2])
        heapq.heappush(maxh, ((-L, -P), P))
        heapq.heappush(minh, ((L, P), P ))
    elif cmd[0] == 'solved':
        solved.add(P)
    else:
        rmv(maxh)
        rmv(minh)
        if P == 1: print(maxh[0][1])
        else: print(minh[0][1])