##### Python 3 #####
##### Runtime 922ms, Memory 24.8MB #####

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # 무방향 tree 만듦
        tree = collections.defaultdict(list)    
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
            
        # 높이가 가장 작은 트리의 루트를 구하기 위해서는 그 루트값이 가장 중앙값이 되어야함
        # 즉 n이 홀수일 때는 1개, 짝수일 때는 2개의 중앙값을 구하면 됨
        # while문으로 리프노드를 계속 제거하여 중앙값을 구했음
        
        # 첫 시작시 리프노드를 구함
        leaves = []
        for t in tree:
            if len(tree[t]) == 1:
                leaves.append(t)
        
        # 중앙값은 최소 1개 최대 2개 이기 때문에 n > 2 으로 while문 돌림
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            # 무방향 tree이기에 양쪽에서 리프노드 삭제해줌
            for leaf in leaves:
                neighbor = tree[leaf].pop()
                tree[neighbor].remove(leaf)
                
                # 삭제한 후 이웃값이 리프노드인지 확인
                if len(tree[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
            
        return leaves
            
                