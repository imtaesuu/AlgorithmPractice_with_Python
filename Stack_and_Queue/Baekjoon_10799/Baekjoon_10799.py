##### My code #####
##### Runtime 92ms, Memory 29632KB #####

import sys

def input():
  return sys.stdin.readline().rstrip()

stack = []
arr = input()
prev, res = '', 0

for s in arr:
  if s == '(':
    stack.append(s)
  else:
    if prev == '(':
      stack.pop()
      res += len(stack)
    else:
      stack.pop()
      res += 1
  prev = s

print(res)