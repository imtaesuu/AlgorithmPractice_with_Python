##### My code #####
##### Runtime 316ms, Memory 60376KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
sprs = deque()
visited = set()

for i in list(map(int, input().split())):
    sprs.append((i, 1))
    visited.add(i)

res, house = 0, 0
while sprs:
    x, num = sprs.popleft()
    for dx in [1, -1]:
        if x+dx in visited:
            continue
        sprs.append((x+dx, num+1))
        visited.add(x+dx)
        res += num
        house += 1
        if house == K:
            sprs = []
            break
print(res)        