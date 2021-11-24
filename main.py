import sys, math
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

#queue = deque([input()])

s = '(0/(0))'
stack, table = [], []
for idx, val in enumerate(s):
    if val == '(':
        stack.append((idx, val))
    elif val == ')':
        tmp = stack.pop()
        table.append((tmp[0], idx))

table.sort(key=lambda x: x[0])
dstc = len(table)
print(dstc, table)
for i in range(dstc):
    a = table[i]
    tmp = s[a[0]+1:]+ s[:a[1]]
    print(tmp)
    for j in range(i+1, dstc+1):
        b = table[j]
        print(tmp[b[0]+1:]+ tmp[:b[1]])
