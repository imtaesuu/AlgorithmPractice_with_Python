##### My code #####
##### Runtime 68ms, Memory 29200KB #####

import sys

def input():
  return sys.stdin.readline().rstrip()

cpts = int(input())
pairs = int(input())

graph = {cpt + 1: [] for cpt in range(cpts)}

for _ in range(pairs):
  cpt1, cpt2 = map(int, input().split())
  if cpt2 not in graph[cpt1]: 
     graph[cpt1] += [cpt2]
     graph[cpt2] += [cpt1]

def dps(start = 1, arrived = []):
  arrived.append(start)
  for cpt in graph[start]:
    if cpt not in arrived:
      arrived = dps(cpt, arrived)
  return arrived

print(len(dps()) - 1)