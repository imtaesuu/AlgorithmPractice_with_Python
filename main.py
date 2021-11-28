import sys, math, itertools
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

# 3 2 3 8 7 1 8
# 0 1 1 0 4 5 4

N = int(input())
towers = list(map(int, input().split()))

table = [0]*N
stack = []
for i in range(N-1, -1, -1):
    while stack and towers[i] > towers[stack[-1]]:
        table[stack.pop()] = i+1
    stack.append(i)
print(' '.join(map(str, table)))