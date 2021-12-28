import sys, datetime , math, itertools, random
from collections import Counter, defaultdict
import heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



N, W = map(int, input().split())
    
# 최대 크기로 리스트 만듦
table = [0]*(N+1)
table[1] = 2
# 연결된 노드의 수, 해당 노드가 루트일 때 자식의 수를 구하는 거
for _ in range(N-1):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1

leaf_nodes = 0
for i in range(1, N+1):
    if table[i] == 1:
        leaf_nodes += 1

print(W/leaf_nodes)
    