import sys, math, itertools
from collections import Counter
import heapq

import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

def rmv(heap, visited):
    while heap and visited[heap[0][1]]:
        heapq.heappop(heap)
    

T = int(input())
for _ in range(T):
    k = int(input())
    maxh, minh = [], []
    visited = [0]*k
    for i in range(k):
        args = input().split()
        arg, num = args[0], int(args[1])
        
        if arg == 'I':
            heapq.heappush(maxh, (-num, i))
            heapq.heappush(minh, (num, i))
        elif arg == 'D':
            rmv(maxh, visited)
            rmv(minh, visited)
            if num == 1 and maxh:
                visited[heapq.heappop(maxh)[1]] = 1
            elif num == -1 and minh:
                visited[heapq.heappop(minh)[1]] = 1
    rmv(maxh, visited)
    rmv(minh, visited)
    if maxh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')