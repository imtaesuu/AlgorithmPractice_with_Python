##### My code #####
##### Runtime 100ms, Memory 32120KB #####

from collections import deque

N, K = map(int, input().split())

people = deque([i+1 for i in range(N)])
rlt = []

while people:
  people.rotate(-(K-1))
  rlt.append(people.popleft())

print("<" + ", ".join(map(str, rlt)) + ">")