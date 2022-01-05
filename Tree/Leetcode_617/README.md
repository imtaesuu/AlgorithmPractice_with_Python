## - Leetcode 617 Merge Two Binary Trees - [Link](https://leetcode.com/problems/merge-two-binary-trees/)
● 입력  
> root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] 

● 출력
> [3,4,5,5,4,null,7]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_617/Leetcode_617.py)

```python
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
            
##### Python 3 #####
##### Runtime 116ms, Memory 15.4MB #####
```

## - **How To Solve**
- 재귀와 스택을 이용하여 풀 수 있는 문제, 반드시 두 방식으로 풀이해 볼 것
- 재귀로 풀이할 때는 TreeNode를 새로 계속 만들어서 넘기는 것이고, stack은 계속 다음것을 쌍으로 묶고 넘긴후
- 최종적으로 root1을 반환