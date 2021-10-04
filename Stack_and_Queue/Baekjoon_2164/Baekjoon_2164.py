from collections import deque

num = int(input())

stack = deque([x+1 for x in reversed(range(num))])

while len(stack) != 1:
  stack.pop()
  stack.appendleft(stack.pop())

print(stack[0])