##### My code #####
##### Runtime 68ms, Memory 29200KB #####

import sys

def input():
  return sys.stdin.readline().rstrip()

alphabet, table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', {}
cnt = int(input())
line = input()

for _ in range(cnt):
  num = int(input())
  table[alphabet[_]] = num 

stack, rlt = [], 0

for s in line:
  if s.isalpha():
    stack.append(table[s])
  else:
    num1 = stack.pop()
    num2 = stack.pop()
    if s == '+':
      stack.append(num2 + num1)
    elif s == '-':
      stack.append(num2 - num1)
    elif s == '*':
      stack.append(num2 * num1)
    elif s == '/':
      stack.append(num2 / num1)

print(f'{stack[0]:.2f}')   