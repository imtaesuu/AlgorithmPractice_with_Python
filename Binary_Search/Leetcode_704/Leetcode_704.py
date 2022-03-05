### Python 3 #####
##### Runtime 248ms, Memory 22.9MB #####

class Solution:
    # idx를 담을 변수를 생성
    idx: int = None
    def search(self, nums: List[int], target: int) -> int:
        
        def fn(left: int, right: int) -> None:
            # left가 right보다 크다면 idx에 -1을 넣음
            if left > right:
                self.idx = -1
                return
            
            # 포인트는 중앙값을 설정한 것, 파이썬에서는 상관없지만 int 자료형의 크기 제한이 있기 때문에
            # left + right 는 오버플로우가 일어날 수도 있음, 따라서 아래와 같이 변형해줌
            mid = left+(right-left)//2
            
            # 대소비교에 따라 다음 리스트의 시작과 끝을 넘겨주면 됨
            if nums[mid] > target:
                fn(left, mid-1)
            elif nums[mid] < target:
                fn(mid+1, right)
            else:
                self.idx = mid
        
        fn(0, len(nums)-1)
        return self.idx