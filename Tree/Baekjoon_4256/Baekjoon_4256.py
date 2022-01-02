##### Python 3 #####
##### Runtime 212ms, Memory 30212KB #####

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def to_postorder(p_start, p_end, i_start, i_end):    
    if p_end < p_start or i_end < i_start:
        return 
    
    root = preorder[p_start]
    # inorder 값에서의 root값의 idx
    # ValueError를 방지하기 위해 미리 테이블을 만들어둠
    # 위치 동기화를 위해 시작 위치를 빼준게 길이
    pos = position[root]
    length = pos - i_start
    
    # 재귀로 왼쪽 오른쪽을 차례로 보내고 출력해줌
    to_postorder(p_start+1, p_start+length, i_start, pos-1)
    to_postorder(p_start+length+1, p_end, pos+1, i_end)
    print(root, end = ' ')

T = int(input())
for _ in range(T):
    N = int(input())

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    position = [0] * (N+1)

    # 미리 inorder의 값들의 위치를 테이블에 넣어둠
    for i in range(N):
        position[inorder[i]] = i
    
    to_postorder(0, N-1, 0, N-1)
    print()