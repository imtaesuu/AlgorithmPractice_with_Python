# import sys, datetime , math, itertools, random
# from collections import Counter, defaultdict, deque
# import heapq
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
import random

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_numbers = [i+j+k+l for i in nums for j in nums for k in nums for l in nums]

answer = input()
number = random.choice(all_numbers)
res = [None, None, None, None]

while True:
    print(res)
    if number == answer:
        print()
        print(number)
        print('정답')
        break


        
    strike, ball = 0, 0
    for i in range(4):
        if number[i] in answer:
            ball += 1
        
        if number[i] == answer[i]:
            strike += 1
            res[i] = number[i]
    
    print()
    print(number)
    print(strike, 'strike ', ball, "ball")
    
    tmp = []
    for i in all_numbers:
        
        if res[0] and i[0] != res[0]:
            continue
        
        if res[1] and i[1] != res[1]:
            continue
            
        if res[2] and i[2] != res[2]:
            continue
            
        if res[3] and i[3] != res[3]:
            continue
            
        tmp.append(i)
    
    all_numbers = tmp
    number = random.choice(all_numbers)


print()


