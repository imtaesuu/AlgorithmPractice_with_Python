##### My code #####
##### Runtime 68ms, Memory 29200KB #####

import sys

def input():
    return sys.stdin.readline().rstrip()

def findVPS(PS):
	stack = []
	
	if not PS:
		return False

	for i in PS:
		if i == '(':
			stack.append('(')
		elif i == ')' and stack:
			stack.pop()
		else:
			return False
	
	return not stack

cnt = int(input())

for _ in range(cnt):
	s = input()

	if findVPS(s):
		print('YES')
	else:
		print('NO')