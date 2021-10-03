import sys

def input():
  return sys.stdin.readline().rstrip()

cnt = int(input())
stack = []

while cnt != 0:
  cmd = input().split()
  cnt -= 1

  if cmd[0] == 'push':
    stack.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  elif cmd[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])