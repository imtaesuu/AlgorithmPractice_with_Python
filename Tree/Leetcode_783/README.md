## - Leetcode 783 Minimum Distance Between BST Nodes - [Link](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)
● 입력  
> root = [1,0,48,null,null,12,49]

● 출력
> 1

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_783/Leetcode_783.py)

```python
class Solution:
    # 재할당을 위해 클래스 범위에서 변수 선언
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        # 왼쪽 노드가 있다면 왼쪽 노드를 보냄
        if root.left:
            self.minDiffInBST(root.left)
        
        # 최초 실행은 루트 노드에서부터 가장 왼쪽에 있는 노드임
        # 값차이를 최소한의 계산으로 확인하기위해 중위순회를 활용
        # 이진 탐색 트리이기에 가능한 방법
        
        # 차이를 구하고 result에 넣어줌
        self.result = min(self.result, root.val - self.prev)
        # 현재 탐색 노드값을 전 탐색 노드값에 넣어줌
        self.prev = root.val
    
        # 오른쪽 노드가 있다면 오른쪽 노드를 보냄
        if root.right:
            self.minDiffInBST(root.right)
        
        return self.result

##### Python 3 #####
##### Runtime 36ms, Memory 13.9MB #####
```

## - **How To Solve**
- 이진 탐색 트리의 구조를 이해하고 이용하여 풀이함
- 루트 노드로부터 바로 오른쪽 노드와 루트 노드의 차이는 최소가 될 수 있음
- 어차피 오른쪽으로 내려가 봤자 차이값이 커지기 때문임
- 따라서 중위순회를 이용하여 탐색하면서 동시에 차이값을 구함
