import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline


candidates = [2,3,5]
target = 8

res, temp = [], []

def dfs(idx, num):
    if num >= target:
        if num == target:
            print("저장")
            res.append(temp[:])
        return

    for i, v in enumerate(candidates[idx:]):
        temp.append(v)
        num += v
        print(i, v, num)
        dfs(i, num)
        temp.pop()
        num -= v

dfs(0, 0)
print(res)


