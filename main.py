import sys, math, itertools
from collections import defaultdict, deque
input = lambda : sys.stdin.readline().rstrip()

#queue = deque([input()])

s = '(((1)))+1'
stack, table = [], []
for idx, val in enumerate(s):
    if val == '(':
        stack.append((idx, val))
    elif val == ')':
        tmp = stack.pop()
        table.append((tmp[0], idx))
res = []
for i in range(1, len(table)+1):
    for j in itertools.combinations(table, i):
        n = sorted([e for each in j for e in each], reverse = True)
        tmp = list(s)
        
        for k in n:
            del tmp[k]
        res.append(''.join(tmp))
res = set(res)
print(*sorted(res), sep = '\n')