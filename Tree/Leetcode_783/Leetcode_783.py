##### Python 3 #####
##### Runtime 36ms, Memory 13.9MB #####

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