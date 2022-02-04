##### Python 3 #####
##### Runtime 50ms, Memory 13.9MB #####

class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 노드가 None이면 return
        if root is None:
            return 
        
        # 이진 탐색 트리로 이루어져 있기 때문에 루트의 오른쪽 자식은 무조건 루트보다 큼
        # 이러한 원리를 이용하여 root의 오른쪽 값을 계속 더하여 누적값과 현재값을 이용하여 풀이
        
        # 가장 먼저 오른쪽 노드로 이동
        self.bstToGst(root.right)
        # 누적값에 현재값을 더함
        self.val += root.val
        # 현재값을 누적값으로 바꿈
        root.val = self.val
        # 왼쪽 노드로 이동
        self.bstToGst(root.left)
        
        return root