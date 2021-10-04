##### My code #####
##### Runtime 264ms, Memory 35152KB #####

import sys

def input():
  return sys.stdin.readline().rstrip()

cnt = int(input())

stack, table = [], []

for _ in range(cnt):
  num = int(input())
  table.append(num)

idx, rlt = 0, []

for n in range(1, cnt + 1):
  stack.append(n)
  rlt.append("+")
  while stack and stack[-1] == table[idx]:
    stack.pop()
    idx += 1
    rlt.append("-")

if stack:
  print("NO")
else:
  for s in rlt:
    print(s)