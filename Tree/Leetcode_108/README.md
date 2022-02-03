## - Leetcode 108 Convert Sorted Array to Binary Search Tree - [Link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
● 입력  
> nums = [-10,-3,0,5,9]

● 출력
> [0,-3,9,-10,null,5]

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Leetcode_108/Leetcode_108.py)

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # nums를 반으로 나눔
        middle = len(nums)//2
        
        # 중앙값을 val로 갖는 노드를 생성
        node = TreeNode(nums[middle])
        
        # nums는 정렬된 상태이기 때문에 중앙값을 기준으로 left, right를 나눔
        node.left = self.sortedArrayToBST(nums[:middle])
        node.right = self.sortedArrayToBST(nums[middle+1:])
        
        return node

##### Python 3 #####
##### Runtime 115ms, Memory 15.6MB #####
```

## - **How To Solve**
- 정렬된 배열이기에 중앙값을 기준으로 left, right을 나누어 재귀하여 풀이함
- 만약 nums가 정렬되어 있지 않다면 값을 정렬하여 풀이하면 됨
- 이진 탐색 트리는 정렬된 상태이기 때문에 크기 비교에 너무 집착하여 문제를 정확히 이해하지 못했음