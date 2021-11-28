##### PyPy3 #####
##### Runtime 284ms, Memory 222392KB #####

N = int(input())
towers = list(map(int, input().split()))
table, satck = [0]*N, []

for i in range(N-1, -1, -1):
    while stack and towers[i] >= towers[stack[-1]]:
        table[stack.pop()] = i+1
    stack.append(i)
print(' '.join(map(str, table)))