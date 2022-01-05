##### Python 3 #####
##### Runtime 116ms, Memory 15.4MB #####

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 둘다 존재 None이 아니여야지만 val값이 있음
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            
            #노드에 각 val값을 더하고 왼쪽은 왼쪽걸로 오른쪽은 오른쪽으로 재귀 보냄
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node    
        else:
            # or은 and와 다르게 둘중에 하나면 참이면 참값을 반환시킴
            return root1 or root2