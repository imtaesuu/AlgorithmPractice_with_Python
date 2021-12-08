##### Python 3 #####
##### Runtime 876ms, Memory 31268KB #####

import sys, heapq 
input = sys.stdin.readline

N = int(input())
table = list(map(int, input().split()))
heapq.heapify(table)

for _ in range(N-1):
    elements = map(int, input().split())    
    for e in elements:
        if table[0] < e:
            heapq.heappushpop(table, e)
print(table[0])