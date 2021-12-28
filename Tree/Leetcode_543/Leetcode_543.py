##### Python 3 #####
##### Runtime 44ms, Memory 16.3MB #####

class Solution:
    # 중첩함수에서의 재할당을 위해 class 내부에 변수 선언
    distance: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            # 리프 노드일 때 -1을 return 하여 페널티 부여
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 왼쪽 노드와 오른쪽 노드의 길이를 구하고, 현재 노드에서의 최장 길이를 상태값으로 전환
            self.distance = max(self.distance, left + right + 2)
            return max(left, right) + 1
        
        dfs(root)
        return self.distance