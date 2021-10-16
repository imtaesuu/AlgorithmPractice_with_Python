##### My code #####
##### Runtime 520ms, Memory 55996KB #####

import sys

def input():
  return sys.stdin.readline().rstrip()

node = int(input())
graph = {key + 1 : [] for key in range(node)}
res = [0 for _ in range(node)]

for _ in range(node - 1):
  node1, node2 = map(int, input().split())
  if node1 not in graph[node2]:
    graph[node1] += [node2]
    graph[node2] += [node1]

def dps():
  arrived = [0]*(node+1)
  stack = [1]

  while stack:
    key = stack.pop()
    if not arrived[key]:
      arrived[key] = 1
      for val in graph[key]:
        stack.append(val)
        if res[val - 1] == 0:
          res[val - 1] = key
  
dps()
for child in res[1:]: print(child)