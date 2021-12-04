import sys, math, itertools
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
table = [input() for _ in range(N)]
dic = defaultdict(int)

cnt = 0

for _ in range(M):
    string = input()
    dic[string] += 1

for key in dic.keys():
    if key in table:
        cnt += dic[key]
print(cnt)