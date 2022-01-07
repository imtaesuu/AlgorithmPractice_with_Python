## - Leetcode 110 Balanced Binary Tree - [Link](https://leetcode.com/problems/balanced-binary-tree/)
● 입력  
> root = [1,2,2,3,3,null,null,4,4]

● 출력
> false

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_110/Leetcode_110.py)

```python
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
        
##### Python 3 #####
##### Runtime 48ms, Memory 19.3MB #####
```

## - **How To Solve**
- dfs를 이용하여 트리의 깊이 구하는 것 처럼 풀이함
- 중간에 좌측과 우측의 차이가 1 이상일 때 res 값이 false가 되는 것만 추가했음
- 포인트는 리프노드까지 간 후부터가 시작이라는 것과 올라갈 때마다 레벨이 증가하므로 +1 해주는 것