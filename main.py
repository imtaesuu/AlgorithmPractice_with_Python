import sys, math, itertools
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

elements = list('a-b-c-d-e-f-g') 
stack, res = [], []
table = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}


for e in elements:
    if e.isalpha():
        res.append(e)
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while True:
            tmp = stack.pop()    
            if tmp == '(':
                break
            res.append(tmp)
    else:
        while stack and table[stack[-1]] >= table[e]:
            res.append(stack.pop())
        stack.append(e)

while stack:
    res.append(stack.pop())

print(''.join(res))  
