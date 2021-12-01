##### Python 3 #####
##### Runtime 500ms, Memory 57692KB #####

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
circles = []

for _ in range(N):
    x, r = map(int, input().split())
    circles.append((x - r, x + r))

circles.sort(key = lambda x : x[0])

for i in range(N-1):
    l1, r1 = circles[i]
    l2, r2 = circles[i+1]
    if l1 == l2 or r1 == r2 or r1 == l1 or l2 < r1 < r2:
        print('NO')
        sys.exit(0)           
print('YES')   