##### My code #####
##### Runtime 324ms, Memory 32684KB #####

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

node, line, start = map(int, input().split())
graph = {key + 1 : [] for key in range(node)}

for _ in range(line):
  node1, node2 = map(int, input().split())
  if node1 not in graph[node2]:
    graph[node1] += [node2]
    graph[node2] += [node1]

def dfs():
  arrived = []
  stack = [start]
  table = {key : list(reversed(sorted(val))) for key, val in graph.items()}

  while stack:
    key = stack.pop()
    if key not in arrived:
      arrived.append(key)
      for val in table[key]:
        stack.append(val)
  return arrived

def bfs():
  arrived = [start]
  queue = deque([start])
  table = {key : list(sorted(val)) for key, val in graph.items()}

  while queue:
    key = queue.popleft()
    for val in table[key]:
      if val not in arrived:
        arrived.append(val)
        queue.append(val)
  return arrived

print(*dfs())
print(*bfs())