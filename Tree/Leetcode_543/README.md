## - Leetcode 543 Diameter of Binary Tree - [Link](https://leetcode.com/problems/diameter-of-binary-tree/)
● 입력  
> root = [1,2,3,4,5]  

● 출력
> 3  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_543/Leetcode_543.py)

```python
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
##### Python 3 #####
##### Runtime 44ms, Memory 16.3MB #####
```

## - **How To Solve**
- 문제의 난이도는 easy 이지만 재귀로 풀기 꽤 까다로웠던 문제
- 본인은 리프노드를 만나고 바로 길이 1을 반환하여 풀이하는 것으로 생각해서 구현 방식에서의 코드 가독성이 떨어졌음
- 리프노드에서는 페널티 -1을 부여함으로써 좀더 읽고 이해하기 쉬운 코드가 됨
- 또 중첩함수에서의 변수가 재할당 되지 않고 새로운 id값을 가진 local 변수로 선언되기 때문에 클래스 내부에서 변수 선언