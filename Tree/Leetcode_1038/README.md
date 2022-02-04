## - Leetcode 1038 Binary Search Tree to Greater Sum Tree - [Link](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)
● 입력  
> root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]

● 출력
> [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_1038/Leetcode_1038.py)

```python
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
        
##### Python 3 #####
##### Runtime 50ms, Memory 13.9MB #####
```

## - **How To Solve**
- 이진 탐색 트리의 구조를 이해하고 이용하여 풀이함
- 어차피 현재 노드의 값은 항상 오른쪽 자식 노드값에 영향을 받기 때문에 왼쪽 노드로 이동만 함
- 재귀를 이용하면 왼쪽 노드로 이동하기만 해도 그 노드의 오른쪽 자식의 값과 자신의 값, 누적값을 더함
