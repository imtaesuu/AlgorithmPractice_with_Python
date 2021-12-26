import sys, datetime , math, itertools
from collections import Counter, defaultdict
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



N = int(input())
table = [0]*100001
for _ in range(N-1):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1

Q = int(input())
for _ in range(Q):
    args = list(map(int, input().split()))
    
    if args[0] == 1:
        print('no' if table[args[1]] < 2 else 'yes')
    else:
        print('yes')
    
