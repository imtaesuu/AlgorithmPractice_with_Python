##### My code #####
##### Runtime 14020ms, Memory 226228KB #####

import sys
from collections import deque

def input():
  return sys.stdin.readline()

cmt, line = map(int, input().split())
graph = {key + 1 : [] for key in range(cmt)}

for _ in range(line):
  node1, node2 = map(int, input().split())
  graph[node2] += [node1]

def bfs(start):
  arrived = [0] * (cmt + 1)
  arrived[start] = 1 
  q = deque([start])
  cnt = 0

  while q:
    temp = q.popleft()
    for node in graph[temp]:
      if not arrived[node]:
        q.append(node)
        arrived[node] = 1
        cnt += 1
  return cnt

max_num = 0
res = []
for i in range(cmt):
  if graph[i + 1]:
    num = bfs(i + 1)
    if max_num <= num:
      if max_num < num:
        res.clear()
      max_num = num
      res.append(i + 1)
print(*res)