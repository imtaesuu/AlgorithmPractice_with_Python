##### Python 3 #####
##### Runtime 48ms, Memory 19.3MB #####

class Solution:
    res = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # node가 없거나 res가 이미 false면 바로 0 반환
            if node is None or not self.res:
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 좌측과 우측의 차이가 1이상이면 res는 false
            if abs(left-right) > 1:
                self.res = False
            
            # 올라갈 때마다 레벨은 1씩 증가하고 좌측과 우측중 깊이가 더 깊은 레벨을 더함
            return max(left, right)+1
        
        dfs(root)
        return self.res