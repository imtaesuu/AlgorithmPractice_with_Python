##### My code #####
##### Runtime 2184ms, Memory 92888KB #####

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

cnt = int(input())
queue = deque()

for _ in range(cnt):
  cmd = input().split()

  if cmd[0] == 'push':
    queue.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(queue))
  elif cmd[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif cmd[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif cmd[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])