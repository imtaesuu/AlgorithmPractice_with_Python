##### Python 3 #####
##### Runtime 115ms, Memory 15.6MB #####

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