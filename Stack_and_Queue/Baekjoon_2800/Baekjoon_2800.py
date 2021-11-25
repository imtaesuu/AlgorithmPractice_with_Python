##### Python 3 #####
##### Runtime 68ms, Memory 29452KB #####

import itertools
s = input()
stack, table = [], []
# 괄호쌍을 테이블에 담기
for idx, val in enumerate(s):
    if val == '(':
        stack.append((idx, val))
    elif val == ')':
        tmp = stack.pop()
        table.append((tmp[0], idx))

#itertools의 조합을 이용하여 경우의 수를 구한다음 
#인덱스값이 넘어가지 않도록 하기 위하여 내림차순으로 정렬
res = []
for i in range(1, len(table)+1):
    for j in itertools.combinations(table, i):
        n = sorted([e for each in j for e in each], reverse = True)
        tmp = list(s)
        
        for k in n:
            del tmp[k]
        res.append(''.join(tmp))
print(*sorted(set(res)), sep = '\n')